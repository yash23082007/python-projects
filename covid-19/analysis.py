"""
analysis.py
-------------------------
Performs statistical analysis on the COVID-19 dataset.
"""

import numpy as np
import pandas as pd


def total_confirmed(df):
    total = df["Confirmed"].sum()
    print(f"Total Confirmed Cases : {total:,}")
    return total


def total_deaths(df):
    total = df["Deaths"].sum()
    print(f"Total Deaths : {total:,}")
    return total


def total_recovered(df):
    total = df["Recovered"].sum()
    print(f"Total Recovered : {total:,}")
    return total


def total_active(df):
    total = df["Active"].sum()
    print(f"Total Active Cases : {total:,}")
    return total


def mortality_rate(df):
    confirmed = df["Confirmed"].sum()
    deaths = df["Deaths"].sum()

    rate = (deaths / confirmed) * 100

    print(f"Mortality Rate : {rate:.2f}%")
    return rate


def recovery_rate(df):
    confirmed = df["Confirmed"].sum()
    recovered = df["Recovered"].sum()

    rate = (recovered / confirmed) * 100

    print(f"Recovery Rate : {rate:.2f}%")
    return rate


def statistics(df):

    print("\nStatistics")
    print("-" * 50)

    print("Mean Confirmed :", np.mean(df["Confirmed"]))
    print("Median Confirmed :", np.median(df["Confirmed"]))
    print("Maximum :", np.max(df["Confirmed"]))
    print("Minimum :", np.min(df["Confirmed"]))
    print("Standard Deviation :", np.std(df["Confirmed"]))


def top_10_confirmed(df):

    print("\nTop 10 Countries (Confirmed Cases)")
    print("-" * 50)

    top = (
        df.groupby("Country")["Confirmed"]
        .max()
        .sort_values(ascending=False)
        .head(10)
    )

    print(top)

    return top


def top_10_deaths(df):

    print("\nTop 10 Countries (Deaths)")
    print("-" * 50)

    top = (
        df.groupby("Country")["Deaths"]
        .max()
        .sort_values(ascending=False)
        .head(10)
    )

    print(top)

    return top


def top_10_recovered(df):

    print("\nTop 10 Countries (Recovered)")
    print("-" * 50)

    top = (
        df.groupby("Country")["Recovered"]
        .max()
        .sort_values(ascending=False)
        .head(10)
    )

    print(top)

    return top


def india_data(df):

    print("\nIndia Summary")
    print("-" * 50)

    india = df[df["Country"] == "India"]

    print(india.tail())

    return india


def country_summary(df, country):

    print(f"\n{country} Summary")
    print("-" * 50)

    result = df[df["Country"] == country]

    print(result.tail())

    return result


def daily_cases(df):

    daily = (
        df.groupby("Date")["Confirmed"]
        .sum()
        .reset_index()
    )

    return daily


def monthly_cases(df):

    temp = df.copy()

    temp["Month"] = temp["Date"].dt.to_period("M")

    monthly = (
        temp.groupby("Month")["Confirmed"]
        .sum()
        .reset_index()
    )

    print("\nMonthly Cases")
    print(monthly)

    return monthly


def full_analysis(df):

    print("=" * 60)
    print("COVID-19 DATA ANALYSIS")
    print("=" * 60)

    total_confirmed(df)
    total_deaths(df)
    total_recovered(df)
    total_active(df)

    print()

    mortality_rate(df)
    recovery_rate(df)

    statistics(df)

    top_10_confirmed(df)
    top_10_deaths(df)
    top_10_recovered(df)