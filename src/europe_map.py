import geopandas as gpd


def create_europe_map(
    df,
    year,
    column
):

    europe = gpd.read_file(
        gpd.datasets.get_path(
            "naturalearth_lowres"
        )
    )

    europe = europe.rename(
        columns={
            "name": "country"
        }
    )

    data_year = df[
        df["year"] == year
    ]

    merged = europe.merge(
        data_year,
        on="country",
        how="left"
    )

    return merged