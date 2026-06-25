import customtkinter as ctk
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from data_loader import load_data
from top10 import get_top10

from gui.styles import *


class Top10Frame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.df = load_data()

        # =====================================
        # TYTUŁ
        # =====================================

        title = ctk.CTkLabel(
            self,
            text="Ranking TOP 10 krajów",
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
                "Ranking umożliwia porównanie dziesięciu krajów "
                "osiągających najwyższe lub najniższe wartości "
                "wybranego wskaźnika w określonym roku."
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

        # ----------------------------

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

        # ----------------------------

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
                str(year)
                for year in years
            ],
            width=220
        )

        self.year_menu.pack(
            anchor="w",
            padx=20,
            pady=(5, 15)
        )

        # ----------------------------

        order_label = ctk.CTkLabel(
            controls,
            text="Rodzaj rankingu:",
            font=TEXT_FONT
        )

        order_label.pack(
            anchor="w",
            padx=20
        )

        self.order_menu = ctk.CTkOptionMenu(
            controls,
            values=[
                "Największe",
                "Najmniejsze"
            ],
            width=220
        )

        self.order_menu.pack(
            anchor="w",
            padx=20,
            pady=(5, 15)
        )

        # ----------------------------

        button = ctk.CTkButton(
            controls,
            text="Generuj ranking",
            command=self.show_top10,
            font=BUTTON_FONT,
            height=40
        )

        button.pack(
            padx=20,
            pady=(0, 20)
        )

        # =====================================
        # PANEL WYKRESU
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

    def show_top10(self):

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

        selected_metric = self.metric_menu.get()

        selected_year = int(
            self.year_menu.get()
        )

        metric_map = {

            "OZE": "oze_share",

            "Energia": "energy_price",

            "Inflacja": "inflation",

            "PKB": "gdp_per_capita"

        }

        column = metric_map[
            selected_metric
        ]

        selected_order = self.order_menu.get()

        ascending = (
            selected_order == "Najmniejsze"
        )

        top10 = get_top10(
            self.df,
            selected_year,
            column,
            ascending=ascending
        )

        fig, ax = plt.subplots(
            figsize=(10, 6)
        )

        ax.barh(
            top10["country"],
            top10[column]
        )

        ax.invert_yaxis()

        ax.set_title(
            f"TOP 10 krajów - {selected_metric} ({selected_year})"
        )

        axis_labels = {

            "OZE": "Udział OZE w miksie energetycznym (%)",

            "Energia": "Cena energii (EUR/kWh)",

            "Inflacja": "Inflacja (%)",

            "PKB": "PKB per capita (EUR)"

        }

        ax.set_xlabel(
            axis_labels[selected_metric]
        )

        for i, value in enumerate(
            top10[column]
        ):

            ax.text(
                value,
                i,
                f"{value:.2f}",
                va="center"
            )

        plt.tight_layout()

        canvas = FigureCanvasTkAgg(
            fig,
            master=self.chart_frame
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )