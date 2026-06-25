import customtkinter as ctk

from gui.styles import *


class ConclusionsFrame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        # =====================================
        # TYTUŁ
        # =====================================

        title = ctk.CTkLabel(
            self,
            text="Wnioski końcowe",
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
                "Podsumowanie najważniejszych rezultatów uzyskanych "
                "podczas analizy danych dotyczących udziału OZE, "
                "cen energii elektrycznej oraz czynników ekonomicznych "
                "w krajach Europy."
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
        # PANEL
        # =====================================

        panel = ctk.CTkFrame(
            self,
            corner_radius=CARD_CORNER_RADIUS
        )

        panel.pack(
            fill="both",
            expand=True,
            padx=PAGE_PADX,
            pady=(0, PAGE_PADY)
        )

        textbox = ctk.CTkTextbox(
            panel,
            font=TEXT_FONT
        )

        textbox.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        conclusions_text = """
══════════════════════════════════════════════════════
                     CEL PROJEKTU
══════════════════════════════════════════════════════

Celem projektu było zbadanie zależności pomiędzy udziałem
energii ze źródeł odnawialnych (OZE) a cenami energii
elektrycznej w krajach Europy.

W analizie wykorzystano dane dotyczące:

• udziału OZE,
• cen energii elektrycznej,
• inflacji,
• PKB per capita.

══════════════════════════════════════════════════════
                NAJWAŻNIEJSZE WNIOSKI
══════════════════════════════════════════════════════

✓ Sam udział OZE nie wyjaśnia zmian cen energii.

✓ Ceny energii są zjawiskiem wieloczynnikowym.

✓ Dodanie inflacji oraz PKB per capita znacząco
  poprawiło skuteczność modeli.

✓ Największy wpływ na model miały zmienne ekonomiczne.

✓ Modele trenowane na danych sprzed kryzysu
  osiągały bardziej stabilne wyniki.

══════════════════════════════════════════════════════
              KRYZYS ENERGETYCZNY
══════════════════════════════════════════════════════

Lata 2021–2023 znacząco zaburzyły wcześniejsze zależności
ekonomiczne.

Model trenowany wyłącznie na danych historycznych
(do 2020 roku) uzyskał lepsze wyniki predykcyjne.

══════════════════════════════════════════════════════
                 PREDYKCJA
══════════════════════════════════════════════════════

Prognozy wykonano przy użyciu regresji liniowej.

Model umożliwia prognozowanie cen energii
na kolejne 5 lat dla wybranego kraju.

══════════════════════════════════════════════════════
                OGRANICZENIA
══════════════════════════════════════════════════════

• ograniczona liczba zmiennych,

• brak cen gazu,

• brak emisji CO₂,

• brak danych o imporcie energii,

• uproszczone założenia prognostyczne.

══════════════════════════════════════════════════════
                 PODSUMOWANIE
══════════════════════════════════════════════════════

Przeprowadzona analiza wykazała, że ceny energii
elektrycznej zależą od wielu czynników gospodarczych
i energetycznych.

Najlepsze rezultaty uzyskano po uwzględnieniu
zmiennych ekonomicznych obok udziału OZE.

Uzyskany model może stanowić punkt wyjścia do
dalszych analiz i rozbudowy o dodatkowe dane.
"""

        textbox.insert(
            "1.0",
            conclusions_text
        )

        textbox.configure(
            state="disabled"
        )