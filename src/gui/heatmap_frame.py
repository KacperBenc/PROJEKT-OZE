import customtkinter as ctk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from data_loader import load_data

from heatmaps import create_heatmap


class HeatmapFrame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.df = load_data()

        title = ctk.CTkLabel(
            self,
            text="Heatmapy",
            font=("Arial", 24, "bold")
        )

        title.pack(
            pady=20
        )

        self.option_menu = ctk.CTkOptionMenu(
            self,
            values=[
                "OZE",
                "Energia",
                "Inflacja",
                "PKB"
            ]
        )

        self.option_menu.pack(
            pady=10
        )

        show_button = ctk.CTkButton(
            self,
            text="Pokaż",
            command=self.show_heatmap
        )

        show_button.pack(
            pady=10
        )

        self.chart_frame = ctk.CTkFrame(self)

        self.chart_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    def show_heatmap(self):

        for widget in self.chart_frame.winfo_children():

            widget.destroy()

        selected = self.option_menu.get()

        if selected == "OZE":

            fig = create_heatmap(
                self.df,
                "oze_share",
                "Udział OZE w Europie",
                "YlGn",
                annot=True,fmt=".2f"
            )

        elif selected == "Energia":

            fig = create_heatmap(
                self.df,
                "energy_price",
                "Ceny energii",
                "RdYlGn_r",
                annot=True,fmt=".3f"
            )

        elif selected == "Inflacja":

            fig = create_heatmap(
                self.df,
                "inflation",
                "Inflacja",
                "RdYlGn_r",
                annot=True,fmt=".2f"
            )

        else:

            fig = create_heatmap(
                self.df,
                "gdp_per_capita",
                "PKB per capita",
                "RdYlGn_r",
               annot= False,
               
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