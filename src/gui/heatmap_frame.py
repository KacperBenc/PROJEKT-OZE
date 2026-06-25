import customtkinter as ctk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from data_loader import load_data
from heatmaps import create_heatmap

from gui.styles import *


class HeatmapFrame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.df = load_data()

        # =====================================
        # TYTUŁ
        # =====================================

        title = ctk.CTkLabel(
            self,
            text="Heatmapy",
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
                "Mapa ciepła umożliwia szybkie porównanie wartości "
                "wybranego wskaźnika pomiędzy krajami Europy "
                "w kolejnych latach. Intensywność koloru odpowiada "
                "wartości analizowanej zmiennej."
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

        option_label = ctk.CTkLabel(
            controls,
            text="Wybierz wskaźnik:",
            font=TEXT_FONT
        )

        option_label.pack(
            anchor="w",
            padx=20
        )

        self.option_menu = ctk.CTkOptionMenu(
            controls,
            values=[
                "OZE",
                "Energia",
                "Inflacja",
                "PKB"
            ],
            width=220
        )

        self.option_menu.pack(
            anchor="w",
            padx=20,
            pady=(5, 15)
        )

        show_button = ctk.CTkButton(
            controls,
            text="Generuj heatmapę",
            command=self.show_heatmap,
            font=BUTTON_FONT,
            height=40
        )

        show_button.pack(
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

    # =========================================

    def show_heatmap(self):

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
            pady=(15, 5)
        )

        selected = self.option_menu.get()

        if selected == "OZE":

            fig = create_heatmap(
                self.df,
                "oze_share",
                "Udział OZE w Europie",
                "YlGn",
                annot=True,
                fmt=".2f"
            )

        elif selected == "Energia":

            fig = create_heatmap(
                self.df,
                "energy_price",
                "Ceny energii",
                "RdYlGn_r",
                annot=True,
                fmt=".3f"
            )

        elif selected == "Inflacja":

            fig = create_heatmap(
                self.df,
                "inflation",
                "Inflacja",
                "RdYlGn_r",
                annot=True,
                fmt=".2f"
            )

        else:

            fig = create_heatmap(
                self.df,
                "gdp_per_capita",
                "PKB per capita",
                "RdYlGn_r",
                annot=False
            )

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