"""
clean_data.py
-------------------------
Functions for cleaning and preprocessing the COVID-19 dataset.
"""

import pandas as pd


def remove_duplicates(df):
    """
    Remove duplicate rows.
    """
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)

    print(f"Duplicate Rows Removed : {before - after}")

    return df


def fill_missing_values(df):
    """
    Fill missing values.
    """
    df = df.fillna(0)

    print("Missing values filled with 0.")

    return df


def convert_date(df):
    """
    Convert Date column to datetime.
    """

    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])
        print("Date column converted to datetime.")

    return df


def rename_columns(df):
    """
    Rename long column names.
    """

    rename_dict = {
        "Country/Region": "Country",
        "Province/State": "State",
        "Confirmed": "Confirmed",
        "Deaths": "Deaths",
        "Recovered": "Recovered",
        "Active": "Active"
    }

    df.rename(columns=rename_dict, inplace=True)

    print("Columns renamed.")

    return df


def remove_negative_values(df):
    """
    Remove rows with negative values
    from numeric columns.
    """

    numeric_cols = [
        "Confirmed",
        "Deaths",
        "Recovered",
        "Active"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df = df[df[col] >= 0]

    print("Negative values removed.")

    return df


def sort_by_date(df):
    """
    Sort dataset by Date.
    """

    if "Date" in df.columns:
        df = df.sort_values("Date")

    return df


def reset_index(df):
    """
    Reset dataframe index.
    """

    df.reset_index(drop=True, inplace=True)

    return df


def clean_dataset(df):
    """
    Perform complete data cleaning.
    """

    print("=" * 50)
    print("Cleaning Dataset...")
    print("=" * 50)

    df = remove_duplicates(df)
    df = fill_missing_values(df)
    df = convert_date(df)
    df = rename_columns(df)
    df = remove_negative_values(df)
    df = sort_by_date(df)
    df = reset_index(df)

    print("\nCleaning Completed Successfully!")

    return df


if __name__ == "__main__":

    from load_data import load_dataset

    df = load_dataset()

    if df is not None:

        df = clean_dataset(df)

        print("\nCleaned Dataset")

        print(df.head())