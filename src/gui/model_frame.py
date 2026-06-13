import customtkinter as ctk

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from data_loader import load_data

from model_info import get_model_info


class ModelFrame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        df = load_data()

        model_info = get_model_info(df)

        # ======================
        # Tytuł
        # ======================

        title = ctk.CTkLabel(
            self,
            text="Informacje o modelu",
            font=("Arial", 24, "bold")
        )

        title.pack(
            pady=20
        )

        # ======================
        # Metryki modelu
        # ======================

        metrics_text = f"""
Model trenowany na danych bez kryzysu (do 2020 roku)

------------------------------------------------

Średnie R²:
{model_info['r2_mean']:.3f}

Odchylenie standardowe R²:
{model_info['r2_std']:.3f}

Minimalne R²:
{model_info['r2_min']:.3f}

Maksymalne R²:
{model_info['r2_max']:.3f}

------------------------------------------------

Średnie MAE:
{model_info['mae_mean']:.4f}

Średnie RMSE:
{model_info['rmse_mean']:.4f}
"""

        metrics_label = ctk.CTkLabel(
            self,
            text=metrics_text,
            justify="left"
        )

        metrics_label.pack(
            pady=10
        )

        # ======================
        # Dane do wykresu
        # ======================

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

        # ======================
        # Ramka wykresu
        # ======================

        chart_frame = ctk.CTkFrame(self)

        chart_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # ======================
        # Wykres
        # ======================

        fig, ax = plt.subplots(
            figsize=(8, 4)
        )

        ax.barh(
            labels,
            coeff_df["Percent"]
        )

        ax.set_title(
            "Wpływ zmiennych ekonomicznych na cenę energii"
        )

        ax.set_xlabel(
            "Udział w modelu (%)"
        )

        ax.set_ylabel(
            "Zmienne"
        )

        # wartości na końcach słupków

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

        # ======================
        # Osadzenie wykresu
        # ======================

        canvas = FigureCanvasTkAgg(
            fig,
            master=chart_frame
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )