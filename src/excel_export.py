from pathlib import Path

from openpyxl import Workbook

from openpyxl.chart import (
    LineChart,
    Reference
)


def save_forecast_to_excel(
    forecast_df,
    country
):

    exports_dir = Path(
        "exports"
    )

    exports_dir.mkdir(
        exist_ok=True
    )

    wb = Workbook()

    ws = wb.active

    ws.title = "Forecast"

    headers = list(
        forecast_df.columns
    )

    ws.append(
        headers
    )

    for row in forecast_df.itertuples(
        index=False
    ):

        ws.append(
            list(row)
        )

    chart = LineChart()

    chart.title = (
        f"Prognoza cen energii - {country}"
    )

    chart.y_axis.title = (
        "Cena energii"
    )

    chart.x_axis.title = (
        "Rok"
    )

    data = Reference(
        ws,
        min_col=2,
        min_row=1,
        max_row=len(forecast_df) + 1
    )

    categories = Reference(
        ws,
        min_col=1,
        min_row=2,
        max_row=len(forecast_df) + 1
    )

    chart.add_data(
        data,
        titles_from_data=True
    )

    chart.set_categories(
        categories
    )

    ws.add_chart(
        chart,
        "H2"
    )

    filename = (
        exports_dir
        / f"{country}_forecast.xlsx"
    )

    wb.save(
        filename
    )

    return filename