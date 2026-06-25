import customtkinter as ctk

from PIL import Image
import webbrowser
from pathlib import Path

from data_loader import load_data
from map_generator import generate_map

from gui.styles import *


class MapFrame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.df = load_data()

        # =====================================
        # TYTUŁ
        # =====================================

        title = ctk.CTkLabel(
            self,
            text="Mapa Europy",
            font=TITLE_FONT
        )

        title.pack(
            anchor="w",
            padx=PAGE_PADX,
            pady=(25, 5)
        )

        # =====================================
        # OPIS
        # =====================================

        description = ctk.CTkLabel(
            self,
            text=(
                "Mapa przedstawia przestrzenne zróżnicowanie wybranego "
                "wskaźnika w krajach Europy. "
                "Kolor każdego państwa odpowiada wartości analizowanej "
                "zmiennej dla wybranego roku. "
                "Opcjonalnie można otworzyć interaktywną wersję mapy "
                "w przeglądarce internetowej."
            ),
            justify="left",
            wraplength=900,
            text_color=DESCRIPTION_COLOR,
            font=TEXT_FONT
        )

        description.pack(
            anchor="w",
            padx=PAGE_PADX,
            pady=(0, 20)
        )

        # =====================================
        # PANEL PARAMETRÓW
        # =====================================

        controls = ctk.CTkFrame(
            self,
            corner_radius=CARD_CORNER_RADIUS
        )

        controls.pack(
            fill="x",
            padx=PAGE_PADX,
            pady=(0, 20)
        )

        controls_title = ctk.CTkLabel(
            controls,
            text="Parametry analizy",
            font=SUBTITLE_FONT
        )

        

        controls_title.pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        metric_label = ctk.CTkLabel(
            controls,
            text="Wskaźnik:",
            font=TEXT_FONT
        )

        metric_label.pack(
            anchor="w",
            padx=20
        )

        self.metric_menu = ctk.CTkOptionMenu(
            controls,
            values=[
                "OZE",
                "Energia",
                "Inflacja",
                "PKB"
            ],
            width=220
        )

        self.metric_menu.pack(
            anchor="w",
            padx=20,
            pady=(5, 15)
        )

        year_label = ctk.CTkLabel(
            controls,
            text="Rok:",
            font=TEXT_FONT
        )

        year_label.pack(
            anchor="w",
            padx=20
        )

        years = sorted(
            self.df["year"].unique()
        )

        self.year_menu = ctk.CTkOptionMenu(
            controls,
            values=[
                str(y)
                for y in years
            ],
            width=220
        )

        self.year_menu.pack(
            anchor="w",
            padx=20,
            pady=(5, 15)
        )

        self.browser_var = ctk.BooleanVar()

        browser_checkbox = ctk.CTkCheckBox(
            controls,
            text="Otwórz interaktywną mapę w przeglądarce",
            variable=self.browser_var
        )

        browser_checkbox.pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

        show_button = ctk.CTkButton(
            controls,
            text="Generuj mapę",
            command=self.show_map,
            font=BUTTON_FONT,
            height=40
        )

        show_button.pack(
            padx=20,
            pady=(0, 20)
        )

        # =====================================
        # PANEL WYNIKÓW
        # =====================================

        self.chart_frame = ctk.CTkFrame(
            self,
            corner_radius=CARD_CORNER_RADIUS
        )

        self.chart_frame.pack(
            fill="both",
            expand=True,
            padx=PAGE_PADX,
            pady=(0, PAGE_PADY)
        )

    # =====================================

    def show_map(self):

        for widget in self.chart_frame.winfo_children():

            widget.destroy()

        chart_title = ctk.CTkLabel(
            self.chart_frame,
            text="Wynik analizy",
            font=SUBTITLE_FONT
        )

        chart_title.pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

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

        self.image_label = ctk.CTkLabel(
            self.chart_frame,
            text="",
            image=image
        )

        self.image_label.image = image

        self.image_label.pack(
            pady=10
        )

        if self.browser_var.get():

            html_file = Path(
                html_path
            ).resolve()

            webbrowser.open(
                html_file.as_uri()
            )