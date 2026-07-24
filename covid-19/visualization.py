"""
visualization.py
-----------------------------
Creates and saves graphs using
Matplotlib and Seaborn.
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns

# Folder to save graphs
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Better chart style
sns.set_theme(style="whitegrid")


def bar_chart(top):
    plt.figure(figsize=(10, 6))

    top.plot(kind="bar", color="steelblue")

    plt.title("Top 10 Countries by Confirmed Cases")
    plt.xlabel("Country")
    plt.ylabel("Confirmed Cases")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "bar_chart.png"))
    plt.show()


def line_chart(india):
    plt.figure(figsize=(12, 6))

    plt.plot(
        india["Date"],
        india["Confirmed"],
        color="red",
        linewidth=2
    )

    plt.title("COVID-19 Cases in India")
    plt.xlabel("Date")
    plt.ylabel("Confirmed Cases")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_DIR, "line_chart.png"))

    plt.show()


def histogram(df):

    plt.figure(figsize=(8, 5))

    sns.histplot(
        df["Confirmed"],
        bins=30,
        kde=True
    )

    plt.title("Distribution of Confirmed Cases")

    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_DIR, "histogram.png"))

    plt.show()


def box_plot(df):

    plt.figure(figsize=(8, 4))

    sns.boxplot(x=df["Confirmed"])

    plt.title("Confirmed Cases Box Plot")

    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_DIR, "boxplot.png"))

    plt.show()


def pie_chart(top):

    plt.figure(figsize=(8, 8))

    plt.pie(
        top.values,
        labels=top.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Top 10 Countries")

    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_DIR, "pie_chart.png"))

    plt.show()


def heatmap(df):

    plt.figure(figsize=(8, 6))

    corr = df[
        [
            "Confirmed",
            "Deaths",
            "Recovered",
            "Active"
        ]
    ].corr()

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        linewidths=1
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_DIR, "heatmap.png"))

    plt.show()


def scatter_plot(df):

    plt.figure(figsize=(8, 6))

    sns.scatterplot(
        data=df,
        x="Confirmed",
        y="Deaths",
        alpha=0.6
    )

    plt.title("Confirmed vs Deaths")

    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_DIR, "scatter_plot.png"))

    plt.show()


def recovery_vs_deaths(df):

    plt.figure(figsize=(8, 6))

    sns.scatterplot(
        data=df,
        x="Recovered",
        y="Deaths",
        alpha=0.6
    )

    plt.title("Recovered vs Deaths")

    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_DIR, "recovery_vs_deaths.png"))

    plt.show()


def active_cases_chart(df):

    top = (
        df.groupby("Country")["Active"]
        .max()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(10, 6))

    top.plot(kind="bar", color="orange")

    plt.title("Top 10 Countries by Active Cases")

    plt.xlabel("Country")

    plt.ylabel("Active Cases")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_DIR, "active_cases.png"))

    plt.show()


def deaths_chart(df):

    top = (
        df.groupby("Country")["Deaths"]
        .max()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(10, 6))

    top.plot(kind="bar", color="crimson")

    plt.title("Top 10 Countries by Deaths")

    plt.xlabel("Country")

    plt.ylabel("Deaths")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_DIR, "deaths_chart.png"))

    plt.show()


def create_all_visualizations(df, top_confirmed, india):

    print("=" * 60)
    print("Generating Charts...")
    print("=" * 60)

    bar_chart(top_confirmed)

    line_chart(india)

    histogram(df)

    box_plot(df)

    pie_chart(top_confirmed)

    heatmap(df)

    scatter_plot(df)

    recovery_vs_deaths(df)

    active_cases_chart(df)

    deaths_chart(df)

    print("\nAll charts saved successfully in the output folder.")