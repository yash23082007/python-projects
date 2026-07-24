"""
main.py
---------------------------------
COVID-19 Data Analysis Project

Workflow:
1. Load Dataset
2. Explore Dataset
3. Clean Dataset
4. Analyze Data
5. Generate Visualizations
"""

from load_data import load_dataset, explore_dataset
from clean_data import clean_dataset
from analysis import (
    full_analysis,
    top_10_confirmed,
    india_data
)
from visualization import create_all_visualizations


def main():

    print("=" * 70)
    print("        COVID-19 DATA ANALYSIS USING PYTHON")
    print("=" * 70)

    # -----------------------------
    # Load Dataset
    # -----------------------------
    df = load_dataset()

    if df is None:
        print("Unable to load dataset.")
        return

    # -----------------------------
    # Explore Dataset
    # -----------------------------
    print("\n")
    print("=" * 70)
    print("DATASET EXPLORATION")
    print("=" * 70)

    explore_dataset(df)

    # -----------------------------
    # Clean Dataset
    # -----------------------------
    print("\n")
    print("=" * 70)
    print("DATA CLEANING")
    print("=" * 70)

    df = clean_dataset(df)

    # -----------------------------
    # Statistical Analysis
    # -----------------------------
    print("\n")
    print("=" * 70)
    print("STATISTICAL ANALYSIS")
    print("=" * 70)

    full_analysis(df)

    # -----------------------------
    # Data for Charts
    # -----------------------------
    top_confirmed = top_10_confirmed(df)

    india = india_data(df)

    # -----------------------------
    # Visualizations
    # -----------------------------
    print("\n")
    print("=" * 70)
    print("GENERATING VISUALIZATIONS")
    print("=" * 70)

    create_all_visualizations(
        df,
        top_confirmed,
        india
    )

    print("\n")
    print("=" * 70)
    print("PROJECT COMPLETED SUCCESSFULLY")
    print("=" * 70)
    print("Graphs have been saved inside the output folder.")


if __name__ == "__main__":
    main()