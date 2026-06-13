import pandas as pd


def get_top10(
    df,
    year,
    column,
    ascending=False
):

    filtered = df[
        df["year"] == year
    ]

    top10 = (
        filtered
        .sort_values(
            column,
            ascending=ascending
        )
        .head(10)
    )

    return top10