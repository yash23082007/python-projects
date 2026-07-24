

import os
import pandas as pd


# Dataset folder
DATASET_PATH = r"C:\Users\yash6\.cache\kagglehub\datasets\imdevskp\corona-virus-report\versions\166"


def list_files():
    """
    Display all files in the dataset folder.
    """
    print("=" * 50)
    print("Available Dataset Files")
    print("=" * 50)

    files = os.listdir(DATASET_PATH)

    for i, file in enumerate(files, start=1):
        print(f"{i}. {file}")

    return files


def load_dataset(filename="covid_19_clean_complete.csv"):
    """
    Load a CSV dataset.

    Parameters:
        filename (str): Name of the CSV file

    Returns:
        pandas.DataFrame
    """

    file_path = os.path.join(DATASET_PATH, filename)

    try:
        df = pd.read_csv(file_path)

        print("\nDataset Loaded Successfully!")
        print("File :", filename)
        print("Rows :", df.shape[0])
        print("Columns :", df.shape[1])

        return df

    except FileNotFoundError:
        print("File not found.")
        return None

    except Exception as e:
        print("Error:", e)
        return None


def show_head(df):
    print("\nFirst 5 Rows")
    print("-" * 50)
    print(df.head())


def show_tail(df):
    print("\nLast 5 Rows")
    print("-" * 50)
    print(df.tail())


def show_shape(df):
    print("\nDataset Shape")
    print("-" * 50)
    print(df.shape)


def show_columns(df):
    print("\nColumns")
    print("-" * 50)

    for col in df.columns:
        print(col)


def show_info(df):
    print("\nDataset Information")
    print("-" * 50)
    print(df.info())


def show_summary(df):
    print("\nStatistical Summary")
    print("-" * 50)
    print(df.describe())


def show_missing_values(df):
    print("\nMissing Values")
    print("-" * 50)
    print(df.isnull().sum())


def show_duplicates(df):
    print("\nDuplicate Rows")
    print("-" * 50)
    print(df.duplicated().sum())


def explore_dataset(df):
    """
    Display complete dataset overview.
    """
    show_head(df)
    show_tail(df)
    show_shape(df)
    show_columns(df)
    show_info(df)
    show_summary(df)
    show_missing_values(df)
    show_duplicates(df)


if __name__ == "__main__":

    list_files()

    df = load_dataset()

    if df is not None:
        explore_dataset(df)