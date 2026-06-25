import customtkinter as ctk
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from data_loader import load_data
from model_info import get_model_info

from gui.styles import *


class ModelFrame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        df = load_data()

        model_info = get_model_info(df)

        # ==================================================
        # TYTUŁ
        # ==================================================

        title = ctk.CTkLabel(
            self,
            text="Ocena modelu regresji liniowej",
            font=TITLE_FONT
        )

        title.pack(
            anchor="w",
            padx=PAGE_PADX,
            pady=(25, 5)
        )

        # ==================================================
        # OPIS
        # ==================================================

        description = ctk.CTkLabel(
            self,
            text=(
                "Model regresji liniowej został wytrenowany na danych "
                "historycznych z lat do 2020 roku. "
                "Jakość modelu oceniono na podstawie 50 losowych podziałów "
                "zbioru danych na część treningową i testową. "
                "Poniżej przedstawiono średnie wartości metryk oraz "
                "wpływ poszczególnych zmiennych na przewidywaną cenę energii."
            ),
            justify="left",
            wraplength=950,
            font=TEXT_FONT,
            text_color=DESCRIPTION_COLOR
        )

        description.pack(
            anchor="w",
            padx=PAGE_PADX,
            pady=(0, 20)
        )

        # ==================================================
        # PANEL METRYK
        # ==================================================

        metrics_frame = ctk.CTkFrame(
            self,
            corner_radius=CARD_CORNER_RADIUS
        )

        metrics_frame.pack(
            fill="x",
            padx=PAGE_PADX,
            pady=(0, 20)
        )

        metrics_title = ctk.CTkLabel(
            metrics_frame,
            text="Metryki jakości modelu",
            font=SUBTITLE_FONT
        )

        metrics_title.pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        metrics_text = f"""
Model: Regresja liniowa

Liczba powtórzeń: 50

Dane treningowe:
Lata do 2020 roku

──────────────────────────────

Średnie R²:
{model_info['r2_mean']:.3f}

Odchylenie standardowe:
{model_info['r2_std']:.3f}

Minimalne R²:
{model_info['r2_min']:.3f}

Maksymalne R²:
{model_info['r2_max']:.3f}

──────────────────────────────

Średnie MAE:
{model_info['mae_mean']:.4f}

Średnie RMSE:
{model_info['rmse_mean']:.4f}
"""

        metrics = ctk.CTkTextbox(
            metrics_frame,
            height=250,
            font=TEXT_FONT
        )

        metrics.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        metrics.insert(
            "1.0",
            metrics_text
        )

        metrics.configure(
            state="disabled"
        )

        # ==================================================
        # WYKRES
        # ==================================================

        chart_frame = ctk.CTkFrame(
            self,
            corner_radius=CARD_CORNER_RADIUS
        )

        chart_frame.pack(
            fill="both",
            expand=True,
            padx=PAGE_PADX,
            pady=(0, PAGE_PADY)
        )

        chart_title = ctk.CTkLabel(
            chart_frame,
            text="Wpływ zmiennych na model",
            font=SUBTITLE_FONT
        )

        chart_title.pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        coeff_df = model_info["coefficients"]

        feature_names = {

            "oze_share": "Udział OZE",

            "inflation": "Inflacja",

            "gdp_per_capita": "PKB per capita",

            "year": "Rok"

        }

        labels = [

            feature_names[f]

            for f in coeff_df["Feature"]

        ]

        fig, ax = plt.subplots(
            figsize=(8, 4)
        )

        ax.barh(
            labels,
            coeff_df["Percent"]
        )

        ax.set_title(
            "Wpływ zmiennych ekonomicznych"
        )

        ax.set_xlabel(
            "Wpływ (%)"
        )

        for i, value in enumerate(
            coeff_df["Percent"]
        ):

            ax.text(
                value + 1,
                i,
                f"{value:.1f}%",
                va="center"
            )

        plt.tight_layout()

        canvas = FigureCanvasTkAgg(
            fig,
            master=chart_frame
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )