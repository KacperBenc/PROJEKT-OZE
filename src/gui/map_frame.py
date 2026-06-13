import customtkinter as ctk

from PIL import Image

import webbrowser

from map_generator import generate_map
from pathlib import Path
from data_loader import load_data


class MapFrame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.df = load_data()

        title = ctk.CTkLabel(
            self,
            text="Mapa Europy",
            font=("Arial", 24, "bold")
        )

        title.pack(
            pady=20
        )

        self.metric_menu = ctk.CTkOptionMenu(
            self,
            values=[
                "OZE",
                "Energia",
                "Inflacja",
                "PKB"
            ]
        )

        self.metric_menu.pack(
            pady=10
        )

        years = sorted(
            self.df["year"].unique()
        )

        self.year_menu = ctk.CTkOptionMenu(
            self,
            values=[
                str(y)
                for y in years
            ]
        )

        self.year_menu.pack(
            pady=10
        )

        self.browser_var = ctk.BooleanVar()

        browser_checkbox = ctk.CTkCheckBox(
            self,
            text="Otwórz interaktywną mapę w przeglądarce",
            variable=self.browser_var
        )

        browser_checkbox.pack(
            pady=10
        )

        show_button = ctk.CTkButton(
            self,
            text="Pokaż mapę",
            command=self.show_map
        )

        show_button.pack(
            pady=10
        )

        self.image_label = ctk.CTkLabel(
            self,
            text=""
        )

        self.image_label.pack(
            expand=True,
            pady=20
        )

    def show_map(self):

        metric = self.metric_menu.get()

        year = int(
            self.year_menu.get()
        )

        metric_map = {

            "OZE": (
                "oze_share",
                "Udział OZE (%)",
                "YlGn"
            ),

            "Energia": (
                "energy_price",
                "Cena energii (EUR/kWh)",
                "RdYlGn_r"
            ),

            "Inflacja": (
                "inflation",
                "Inflacja (%)",
                "RdYlGn_r"
            ),

            "PKB": (
                "gdp_per_capita",
                "PKB per capita (EUR)",
                "RdYlGn_r"
            )
        }

        column, title, cmap = metric_map[
            metric
        ]

        fig, html_path, png_path = generate_map(
            self.df,
            year,
            column,
            f"{title} - {year}",
            cmap
        )

        image = ctk.CTkImage(
            light_image=Image.open(
                png_path
            ),
            size=(900, 600)
        )

        self.image_label.configure(
            image=image
        )

        self.image_label.image = image

        if self.browser_var.get():

            html_file = Path(
                html_path
            ).resolve()

            webbrowser.open(
                html_file.as_uri()
            )