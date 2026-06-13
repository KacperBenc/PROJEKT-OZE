import customtkinter as ctk


class ConclusionsFrame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        title = ctk.CTkLabel(
            self,
            text="Wnioski końcowe",
            font=("Arial", 24, "bold")
        )

        title.pack(
            pady=20
        )

        textbox = ctk.CTkTextbox(
            self,
            width=1000,
            height=700
        )

        textbox.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        conclusions_text = """
CEL PROJEKTU

Celem projektu było zbadanie zależności pomiędzy udziałem energii
ze źródeł odnawialnych (OZE) a cenami energii elektrycznej
w krajach europejskich.

W analizie wykorzystano dane Eurostatu dotyczące:
• udziału OZE,
• cen energii elektrycznej,
• inflacji,
• PKB per capita.

------------------------------------------------------------

ANALIZA ZALEŻNOŚCI

Początkowa analiza wykorzystująca wyłącznie udział OZE
nie pozwoliła uzyskać satysfakcjonujących wyników.

Wskazuje to, że ceny energii elektrycznej są zjawiskiem
wieloczynnikowym i zależą od wielu elementów gospodarczych
oraz politycznych.

------------------------------------------------------------

ROZSZERZENIE MODELU

Po dodaniu inflacji oraz PKB per capita
uzyskano znaczącą poprawę jakości modeli.

Największy wpływ na skuteczność predykcji
miało uwzględnienie czynników ekonomicznych,
a nie wyłącznie energetycznych.

------------------------------------------------------------

WPŁYW KRYZYSU ENERGETYCZNEGO

Lata 2021–2023 zostały potraktowane jako okres kryzysu
energetycznego.

Modele trenowane wyłącznie na danych sprzed kryzysu
osiągały bardziej stabilne wyniki predykcyjne.

Oznacza to, że wydarzenia geopolityczne
oraz gwałtowne wzrosty cen surowców
znacząco zaburzyły standardowe zależności ekonomiczne.

------------------------------------------------------------

PREDYKCJA CEN ENERGII

Do prognoz wykorzystano model regresji liniowej
wytrenowany na danych bez okresu kryzysowego.

Prognozy zostały wykonane dla kolejnych 5 lat,
przyjmując rzeczywiste dane z 2024 roku
jako punkt startowy.

------------------------------------------------------------

OGRANICZENIA PROJEKTU

Najważniejsze ograniczenia projektu:

• ograniczona liczba zmiennych,
• brak danych dotyczących cen gazu,
• brak danych dotyczących emisji CO₂,
• brak danych dotyczących importu energii,
• uproszczone założenia prognostyczne.

------------------------------------------------------------

PODSUMOWANIE

Przeprowadzona analiza pokazała,
że ceny energii elektrycznej w Europie
są efektem złożonych zależności
gospodarczych i energetycznych.

Sam udział OZE nie wyjaśnia w pełni
zmienności cen energii.

Uwzględnienie dodatkowych czynników
ekonomicznych pozwala uzyskać
znacznie dokładniejsze modele predykcyjne.
"""

        textbox.insert(
            "1.0",
            conclusions_text
        )

        textbox.configure(
            state="disabled"
        )