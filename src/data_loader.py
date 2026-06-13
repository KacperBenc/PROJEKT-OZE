import pandas as pd


def load_data():
    return pd.read_csv(
        "data/final_dataset.csv"
    )