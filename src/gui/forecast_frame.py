import customtkinter as ctk
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from forecast import predict_country
from excel_export import save_forecast_to_excel
from data_loader import load_data

from gui.styles import *


class ForecastFrame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.df = load_data()

        # =====================================
        # TYTUŁ
        # =====================================

        title = ctk.CTkLabel(
            self,
            text="Predykcja cen energii",
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
                "Moduł umożliwia prognozowanie cen energii "
                "dla wybranego kraju na kolejne 5 lat. "
                "Prognoza została wygenerowana przy użyciu modelu "
                "regresji liniowej wytrenowanego na danych historycznych. "
                "Dodatkowo wyniki można zapisać do pliku Excel."
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
            text="Parametry prognozy",
            font=SUBTITLE_FONT
        )

        controls_title.pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        country_label = ctk.CTkLabel(
            controls,
            text="Wybierz kraj:",
            font=TEXT_FONT
        )

        country_label.pack(
            anchor="w",
            padx=20
        )

        countries = sorted(
            self.df["country"].unique()
        )

        self.country_menu = ctk.CTkOptionMenu(
            controls,
            values=countries,
            width=220
        )

        self.country_menu.pack(
            anchor="w",
            padx=20,
            pady=(5, 15)
        )

        generate_button = ctk.CTkButton(
            controls,
            text="Generuj prognozę",
            command=self.generate_forecast,
            font=BUTTON_FONT,
            height=40
        )

        generate_button.pack(
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

    def generate_forecast(self):

        for widget in self.chart_frame.winfo_children():

            widget.destroy()

        chart_title = ctk.CTkLabel(
            self.chart_frame,
            text="Wynik prognozy",
            font=SUBTITLE_FONT
        )

        chart_title.pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        country = self.country_menu.get()

        forecast_df = predict_country(
            country,
            self.df,
            years=5
        )

        file_path = save_forecast_to_excel(
            forecast_df,
            country
        )

        result_label = ctk.CTkLabel(
            self.chart_frame,
            text=f"✓ Wyniki zapisano do:\n{file_path}",
            text_color="green",
            font=TEXT_FONT
        )

        result_label.pack(
            anchor="w",
            padx=20,
            pady=(0, 10)
        )

        fig, ax = plt.subplots(
            figsize=(8, 5)
        )

        ax.plot(
            forecast_df["year"],
            forecast_df["predicted_energy_price"],
            marker="o",
            linewidth=2
        )

        ax.set_title(
            f"Prognoza cen energii - {country}"
        )

        ax.set_xlabel(
            "Rok"
        )

        ax.set_ylabel(
            "Cena energii (EUR/kWh)"
        )

        ax.grid(
            alpha=0.3
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