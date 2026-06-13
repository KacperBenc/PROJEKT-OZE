# OZE PROJEKT BENC KACPER

Aplikacja desktopowa do analizy zależności pomiędzy udziałem energii odnawialnej (OZE), cenami energii elektrycznej, inflacją oraz PKB per capita w krajach Europy.

## Wymagania

Przed uruchomieniem projektu należy zainstalować:

* Python 3.12 lub nowszy

Sprawdzenie instalacji Pythona:

```powershell
python --version
```

---

## Pierwsze uruchomienie

Przejdź do folderu projektu:

```powershell
cd "C:\ścieżka\do\projektu"
```

Utwórz środowisko wirtualne:

```powershell
python -m venv venv
```

Aktywuj środowisko:

```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
.\venv\Scripts\Activate.ps1
```

Zainstaluj wymagane biblioteki:

```powershell
pip install -r requirements.txt
```

---

## Uruchomienie aplikacji

W folderze głównym projektu uruchom:

```powershell
python src/main.py
```

---

## Aktualizacja danych

Przed uruchomieniem aplikacji można odświeżyć dane Eurostatu poprzez uruchomienie notebooka:

```text
notebook/analiza.ipynb
```

Notebook pobiera najnowsze dane, przetwarza je i zapisuje do:
## UWAGA
JEŻELI MASZ PROBLEM Z DZIAŁANIEM NOTEBOOKA, SPRAWDŹ NA JAKIM KERNELU PYTHONA DZIAŁA (POWINIEN UŻYWAĆ PYTHON ZE SWOJEGO ŚRODOWISKA, NIE GLOBALNEGO!)
```text
data/final_dataset.csv
```

Plik ten jest następnie wykorzystywany przez aplikację desktopową.

---

## Struktura projektu

```text
projekt/
│
├── data/
│   └── final_dataset.csv
│
├── exports/
│   └── pliki Excel z prognozami
│
├── notebook/
│   └── analiza.ipynb
│
├── src/
│   ├── gui/
│   ├── main.py
│   └── ...
│
├── temp/
│   ├── map.html
│   └── map.png
│
├── requirements.txt
│
└── README.md
```

---

## Funkcjonalności aplikacji

* Heatmapy danych dla krajów Europy
* Interaktywne mapy Europy
* Rankingi TOP 10 krajów
* Predykcja cen energii na kolejne 5 lat
* Eksport prognoz do arkusza Excel
* Analiza modelu regresji liniowej
* Wnioski końcowe z projektu

```
```
