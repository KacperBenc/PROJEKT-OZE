import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from forecast import predict_country
from excel_export import save_forecast_to_excel
from data_loader import load_data


class ForecastFrame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.df = load_data()

        title = ctk.CTkLabel(
            self,
            text="Predykcja cen energii",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=20)

        countries = sorted(
            self.df["country"].unique()
        )

        self.country_menu = ctk.CTkOptionMenu(
            self,
            values=countries
        )

        self.country_menu.pack(
            pady=10
        )

        generate_button = ctk.CTkButton(
            self,
            text="Generuj prognozę",
            command=self.generate_forecast
        )

        generate_button.pack(
            pady=20
        )
        
        self.result_label = ctk.CTkLabel(
        self,
        text=""
        )

        self.result_label.pack(
            pady=10
        )

        self.chart_frame = ctk.CTkFrame(
            self
        )

        self.chart_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    def generate_forecast(self):

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

        self.result_label.configure(
            text=f"Zapisano: {file_path}"
        )

        for widget in self.chart_frame.winfo_children():

            widget.destroy()

        fig, ax = plt.subplots(
            figsize=(8, 5)
        )

        ax.plot(
            forecast_df["year"],
            forecast_df["predicted_energy_price"],
            marker="o"
        )

        ax.set_title(
            f"Prognoza cen energii - {country}"
        )

        ax.set_xlabel(
            "Rok"
        )

        ax.set_ylabel(
            "Cena energii"
        )

        ax.grid(
            True
        )

        canvas = FigureCanvasTkAgg(
            fig,
            master=self.chart_frame
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )