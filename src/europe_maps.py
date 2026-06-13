import plotly.express as px


def show_map(
    df,
    year,
    column_name,
    title,
    color_scale
):

    data = df[
        df["year"] == year
    ]

    fig = px.choropleth(
        data,

        locations="country",

        locationmode="country names",

        color=column_name,

        hover_name="country",

        scope="europe",

        color_continuous_scale=color_scale,

        title=f"{title} ({year})"
    )

    fig.update_layout(
        width=1200,
        height=800
    )

    fig.show(
        renderer="browser"
    )