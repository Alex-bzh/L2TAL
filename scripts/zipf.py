#!/usr/bin/env python3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import argparse

def plot_zipf_law(filename):
    # Charger les données
    df = pd.read_csv(filename, sep="\t", header=None, names=["Rank", "Word", "Observed", "Theoretical", "AbsDiff", "MAE"])
    
    # Configurer le style du graphique
    sns.set_theme(style="whitegrid")
    
    # Tracer la loi de Zipf
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=df["Rank"], y=df["Theoretical"], marker="o", markersize=5, label="Fréquence théorique", linestyle="--")
    sns.lineplot(x=df["Rank"], y=df["Observed"], marker="s", markersize=5, label="Fréquence observée", linestyle="-")
    
    # Mise à l'échelle logarithmique
    plt.xscale("log")
    plt.yscale("log")
    
    # Labels et titre
    plt.xlabel("Rang du mot (log)")
    plt.ylabel("Fréquence (log)")
    plt.title("Loi de Zipf - Comparaison des fréquences théoriques et observées")
    plt.legend()
    
    # Sauvegarde du fichier
    output_file = "zipf.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Graphique sauvegardé sous {output_file}")

if __name__ == "__main__":
    # Configuration des arguments de ligne de commande
    parser = argparse.ArgumentParser(description="Tracer la loi de Zipf à partir d'un fichier tabulé et comparer les fréquences théoriques et observées.")
    parser.add_argument("filename", type=str, help="Nom du fichier contenant les données")
    args = parser.parse_args()
    
    plot_zipf_law(args.filename)


