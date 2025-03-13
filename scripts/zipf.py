#!/usr/bin/env python3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import argparse

def plot_zipf_law(filename):
    # Load data
    df = pd.read_csv(filename, sep="\t", header=None, names=["Rank", "Word", "Observed", "Theoretical", "AbsDiff", "MAE"])

    # Convert theoretical frequency to integer (handling commas in numbers)
    df["Theoretical"] = df["Theoretical"].astype(str).str.replace(',', '.').astype(float).astype(int)
    
    # Set theme
    sns.set_theme(style="whitegrid")
    
    # Zipf's law
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=df["Rank"], y=df["Theoretical"], marker="o", markersize=5, label="Fréquence théorique", linestyle="--")
    sns.lineplot(x=df["Rank"], y=df["Observed"], marker="s", markersize=5, label="Fréquence observée", linestyle="-")
    
    # Adjust scale
    plt.xscale("log")
    plt.yscale("log")
    
    # Labels & title
    plt.xlabel("Word rank (log)")
    plt.ylabel("Frequency (log)")
    plt.title("Zipf's law - Comparison of theoretical and observed frequencies")
    plt.legend()
    
    # Save the figure
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Graph saved as zipf.png")

if __name__ == "__main__":
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Plot Zipf's Law from a tab-separated file and save the image.")
    parser.add_argument("filename", type=str, help="Name of the input data file.")
    args = parser.parse_args()
    
    plot_zipf_law(args.filename)
