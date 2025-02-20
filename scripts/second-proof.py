#!/usr/bin/env python3

import argparse
from random import random
from statistics import mean
from typing import Tuple, List

def point(dimensions: int = 2) -> Tuple[float, ...]:
  """Generates random coordinates of a point in n-dimensional space.
    
  Args:
    dimensions: Number of dimensions (default: 2)
    
  Returns:
    Tuple containing the point coordinates
  """
  return tuple(random() for _ in range(dimensions))

def distance(a: Tuple[float, ...], b: Tuple[float, ...]) -> float:
  """Calculates the Euclidean distance between two points in N-dimensional space.
    
  Args:
    a: First point
    b: Second point
  
  Returns:
    Euclidean distance between points
  """
  if len(a) != len(b):
    raise ValueError("Points must have the same number of dimensions")
    
  return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5

def simulation(n: int = 10000, dimensions: int = 2) -> float:
  """Calculates the average distance between two points over n random draws.
    
  Args:
    n: Number of draws (default: 10000)
    dimensions: Number of dimensions (default: 2)
    
  Returns:
    Average distance
  """
  distances = [
    distance(point(dimensions), point(dimensions))
    for _ in range(n)
  ]
  return mean(distances)

def run_simulations(dimensions: int, n_draws: int, n_runs: int) -> List[float]:
  """Runs multiple simulations and returns the results.
    
  Args:
    dimensions: Number of dimensions
    n_draws: Number of draws per simulation
    n_runs: Number of simulations to run
    
  Returns:
    List of average distances obtained
  """
  return [simulation(n_draws, dimensions) for _ in range(n_runs)]

def main():
  parser = argparse.ArgumentParser(
    description="Simulates average distance between random points in N-dimensional space"
  )
  parser.add_argument(
    "-x", "--dimensions",
    type=int,
    default=2,
    help="Number of dimensions (default: 2)"
    )
  parser.add_argument(
    "-r", "--runs",
    type=int,
    default=5,
    help="Number of simulations to run (default: 5)"
  )
  parser.add_argument(
    "-d", "--draws",
    type=int,
    default=10000,
    help="Number of draws per simulation (default: 10000)"
  )
    
  args = parser.parse_args()
    
  results = run_simulations(args.dimensions, args.draws, args.runs)
    
  print(f"\nResults for {args.runs} simulations in {args.dimensions}D space "
    f"with {args.draws} draws per simulation:")

  for i, result in enumerate(results, 1):
    print(f"Simulation {i}: {result:.4f}")

  print(f"\nGlobal average: {mean(results):.4f}")

if __name__ == "__main__":
  main()
