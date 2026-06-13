import customtkinter as ctk

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from data_loader import load_data

from top10 import get_top10


class Top10Frame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.df = load_data()

        title = ctk.CTkLabel(
            self,
            text="TOP 10 krajów",
            font=("Arial", 24, "bold")
        )

        title.pack(
            pady=20
        )

        # --------------------
        # wybór wskaźnika
        # --------------------

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

        # --------------------
        # wybór roku
        # --------------------

        years = sorted(
            self.df["year"]
            .unique()
        )

        self.year_menu = ctk.CTkOptionMenu(
            self,
            values=[
                str(year)
                for year in years
            ]
        )

        self.year_menu.pack(
            pady=10
        )
        self.order_menu = ctk.CTkOptionMenu(
        self,
        values=[
            "Największe",
            "Najmniejsze"
        ]
    )

        self.order_menu.pack(
            pady=10
        )
        # --------------------
        # przycisk
        # --------------------

        button = ctk.CTkButton(
            self,
            text="Pokaż ranking",
            command=self.show_top10
        )

        button.pack(
            pady=20
        )

        # --------------------
        # miejsce na wykres
        # --------------------

        self.chart_frame = ctk.CTkFrame(
            self
        )

        self.chart_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    def show_top10(self):

        for widget in self.chart_frame.winfo_children():

            widget.destroy()

        selected_metric = (
            self.metric_menu.get()
        )

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
        selected_order = (
            self.order_menu.get()
        )

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
            "Inflacja": "Inflacja dla kraju (%)",
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
            expand=True
        )