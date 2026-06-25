import customtkinter as ctk
from gui.styles import *

class Sidebar(ctk.CTkFrame):

    def __init__(self, master, app):

        super().__init__(
            master,
            width=280,
            corner_radius=0,
            fg_color=SIDEBAR_COLOR
        )
        self.app = app

        self.grid_rowconfigure(8, weight=1)

        self.grid_columnconfigure(0, weight=1)

        # ==========================
        # LOGO
        # ==========================

        logo = ctk.CTkLabel(
            self,
            text="ANALIZA OZE\nI CEN ENERGII",
            font=("Segoe UI", 22, "bold"),
            text_color=TITLE_COLOR
        )

        logo.grid(
            row=0,
            column=0,
            padx=20,
            pady=(30, 10)
        )

        section = ctk.CTkLabel(
            self,
            text="Moduły aplikacji",
            font=("Segoe UI", 14)
        )

        section.grid(
            row=1,
            column=0,
            pady=(0, 20)
        )

        # ==========================
        # MENU
        # ==========================

        self.buttons = {}

        menu = [

            ("Strona główna", app.show_home),

            ("Heatmapy", app.show_heatmaps),

            ("Mapa Europy", app.show_map),

            ("TOP 10 krajów", app.show_top10),

            ("Predykcja", app.show_forecast),

            ("Model", app.show_model),

            ("Wnioski", app.show_conclusions)

        ]

        for index, (text, command) in enumerate(menu):

            button = ctk.CTkButton(

                self,

                text=text,

                height=40,
             
                corner_radius=8,
                fg_color=BUTTON_COLOR,

                hover_color=BUTTON_HOVER,

                text_color="white",
                anchor="w",

                font=("Segoe UI", 15),

                command=lambda c=command, t=text:
                    self.change_page(
                        c,
                        t
                    )

            )

            button.grid(

                row=index + 2,

                column=0,

                sticky="ew",

                padx=20,

                pady=5

            )

            self.buttons[text] = button

        # ==========================
        # STOPKA
        # ==========================

        footer = ctk.CTkLabel(

            self,

            text="Kacper Benc\n2026",

            font=("Segoe UI", 11),

            text_color=DESCRIPTION_COLOR

        )

        footer.grid(

            row=9,

            column=0,

            pady=20

        )

        self.activate(
            "Strona główna"
        )

    # ==============================

    def activate(self, active):

        for name, button in self.buttons.items():

            if name == active:

                button.configure(
                    text=f"▶ {name}",
                    fg_color="#0B5ED7",
                    hover_color="#0A58CA",
                    font=("Segoe UI", 15, "bold")
                )

            else:

                button.configure(
                    text=name,
                    fg_color="#1F6AA5",
                    hover_color="#275EA3",
                    font=("Segoe UI", 15)
                )

    # ==============================

    def change_page(
        self,
        command,
        name
    ):

        self.activate(
            name
        )

        command()