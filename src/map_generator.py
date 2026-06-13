import plotly.express as px


ISO_CODES = {
    'Poland': 'POL',
    'Germany': 'DEU',
    'France': 'FRA',
    'Spain': 'ESP',
    'Italy': 'ITA',
    'Portugal': 'PRT',
    'Belgium': 'BEL',
    'Netherlands': 'NLD',
    'Austria': 'AUT',
    'Czech Republic': 'CZE',
    'Slovakia': 'SVK',
    'Hungary': 'HUN',
    'Romania': 'ROU',
    'Bulgaria': 'BGR',
    'Croatia': 'HRV',
    'Slovenia': 'SVN',
    'Estonia': 'EST',
    'Latvia': 'LVA',
    'Lithuania': 'LTU',
    'Finland': 'FIN',
    'Sweden': 'SWE',
    'Norway': 'NOR',
    'Denmark': 'DNK',
    'Ireland': 'IRL',
    'Luxembourg': 'LUX',
    'Cyprus': 'CYP',
    'Malta': 'MLT',
    'Greece': 'GRC',
    'Albania': 'ALB',
    'Bosnia and Herzegovina': 'BIH',
    'Montenegro': 'MNE',
    'North Macedonia': 'MKD',
    'Serbia': 'SRB',
    'Moldova': 'MDA',
    'Georgia': 'GEO',
    'Iceland': 'ISL',
    'Kosovo': 'XKX'
}


def generate_map(
    df,
    year,
    column,
    title,
    cmap
):

    map_data = df[
        df["year"] == year
    ].copy()

    map_data["iso"] = map_data["country"].map(
        ISO_CODES
    )

    fig = px.choropleth(
        map_data,
        locations="iso",
        color=column,
        hover_name="country",
        color_continuous_scale=cmap,
        scope="europe",
        title=title
    )

    html_path = "temp/map.html"

    png_path = "temp/map.png"

    fig.write_html(
        html_path
    )

    fig.write_image(
        png_path,
        width=1200,
        height=800
    )

    return (
        fig,
        html_path,
        png_path
    )