import customtkinter as ctk


class HomeFrame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        title = ctk.CTkLabel(
            self,
            text="Analiza OZE i Cen Energii",
            font=("Arial", 28, "bold")
        )

        title.pack(
            pady=30
        )

        description = ctk.CTkLabel(
            self,
            text="""
Aplikacja do analizy:
- udziału OZE
- cen energii
- inflacji
- PKB per capita
            """
        )

        description.pack()