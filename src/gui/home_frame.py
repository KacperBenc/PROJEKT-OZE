import customtkinter as ctk


class HomeFrame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        title = ctk.CTkLabel(
            self,
            text="Analiza wpływu OZE na ceny energii elektrycznej",
            font=("Segoe UI", 30, "bold")
        )

        title.pack(
            pady=(40, 10)
        )

        subtitle = ctk.CTkLabel(
            self,
            text=(
                "Aplikacja wspomagająca analizę danych Eurostatu\n"
                "oraz prognozowanie cen energii elektrycznej\n"
                "w krajach Europy."
            ),
            font=("Segoe UI", 16),
            justify="center"
        )

        subtitle.pack(
            pady=(0, 30)
        )

        info = ctk.CTkTextbox(
            self,
            width=850,
            height=350,
            font=("Segoe UI", 15)
        )

        info.pack(
            padx=20,
            pady=20
        )

        info.insert(
            "1.0",
            """

Dostępne funkcje:

• Heatmapy
  Wizualizacja zmian wartości analizowanych wskaźników
  dla krajów Europy w kolejnych latach.

• Mapa Europy
  Przedstawienie wybranego wskaźnika na mapie Europy.

• TOP 10 krajów
  Ranking państw osiągających najwyższe lub najniższe
  wartości wybranego wskaźnika.

• Predykcja
  Prognoza cen energii elektrycznej dla wybranego kraju
  z wykorzystaniem modelu regresji liniowej.

• Model
  Informacje o jakości modelu oraz wpływie
  poszczególnych zmiennych na predykcję.

• Wnioski
  Podsumowanie przeprowadzonej analizy.

Życzymy miłego korzystania z aplikacji.
"""
        )

        info.configure(
            state="disabled"
        )