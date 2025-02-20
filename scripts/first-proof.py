#!/usr/bin/env python3

import argparse
from random import random
from typing import Tuple, List
from statistics import mean, stdev
from dataclasses import dataclass

@dataclass
class SimulationConfig:
  """Configuration for point simulation."""
  draws: int = 10000
  dimensions: int = 2
  threshold: float = 0.001
  n_runs: int = 5

  def __post_init__(self):
    """Validate parameters after initialization."""
    if self.draws <= 0:
      raise ValueError("Number of draws must be positive")
    if self.dimensions <= 0:
      raise ValueError("Number of dimensions must be positive")
    if self.threshold <= 0 or self.threshold >= 0.5:
      raise ValueError("Limit must be between 0 and 0.5")
    if self.n_runs <= 0:
      raise ValueError("Number of runs must be positive")

def generate_point(dimensions: int) -> Tuple[float, ...]:
  """Generate random coordinates of a point in n-dimensional space.
    
  Args:
    dimensions: Number of dimensions in the space
    
  Returns:
    Tuple containing point coordinates
  """
  return tuple(random() for _ in range(dimensions))

def is_near_border(point: Tuple[float, ...], threshold: float) -> bool:
  """Detect if any coordinate of the point is near a border.
    
  Args:
    point: Point to test
    threshold: Detection threshold
      
  Returns:
    True if point is near a border, False otherwise
  """
  return any(value <= threshold or value >= 1 - threshold for value in point)

def run_simulation(config: SimulationConfig) -> float:
  """Run a single simulation.
    
  Args:
    config: Simulation configuration
        
  Returns:
    Percentage of points near borders
  """
  count = sum(
    1 for _ in range(config.draws)
    if is_near_border(
      generate_point(config.dimensions),
      config.threshold
    )
  )
  return (count / config.draws) * 100

def run_multiple_simulations(config: SimulationConfig) -> Tuple[float, float]:
  """Run multiple simulations and calculate statistics.
    
  Args:
    config: Simulation configuration
      
  Returns:
    Tuple containing mean and standard deviation of results
  """
  results = [run_simulation(config) for _ in range(config.n_runs)]
  return mean(results), stdev(results) if len(results) > 1 else 0

def format_results(mean_rate: float, std_dev: float, config: SimulationConfig) -> str:
  """Format simulation results.
    
  Args:
    mean_rate: Mean rate of points near borders
    std_dev: Standard deviation of results
    config: Configuration used
        
  Returns:
    Formatted message with results
  """
  return (
    f"In a {config.dimensions}D unit hypercube, a randomly chosen point has\n"
    f"{mean_rate:.2f}% ± {std_dev:.2f}% chance\n"
    f"of being within {config.threshold} of a dimension's border."
  )

def parse_arguments() -> SimulationConfig:
  """Parse command line arguments.
    
  Returns:
    Simulation configuration
  """
  parser = argparse.ArgumentParser(
    description="Point simulation in a hypercube"
  )
  parser.add_argument(
    "-d", "--draws",
    type=int,
    help="number of draws per simulation",
    default=10000
  )
  parser.add_argument(
    "-x", "--dimensions",
    type=int,
    help="number of dimensions",
    default=2
  )
  parser.add_argument(
    "-t", "--threshold",
    type=float,
    help="detection threshold",
    default=0.001
  )
  parser.add_argument(
    "-r", "--runs",
    type=int,
    help="number of simulations",
    default=5
  )
    
  args = parser.parse_args()
  return SimulationConfig(
    draws=args.draws,
    dimensions=args.dimensions,
    threshold=args.threshold,
    n_runs=args.runs
  )

def main():
  """Main entry point of the program."""
  try:
    config = parse_arguments()
    mean_rate, std_dev = run_multiple_simulations(config)
    print(format_results(mean_rate, std_dev, config))
  except ValueError as e:
    print(f"Error: {e}")
    exit(1)

if __name__ == '__main__':
  main()
