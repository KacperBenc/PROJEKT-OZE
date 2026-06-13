import customtkinter as ctk
from gui.heatmap_frame import HeatmapFrame
from gui.map_frame import MapFrame
from gui.forecast_frame import ForecastFrame
from gui.model_frame import ModelFrame
from gui.top10_frame import Top10Frame
from gui.map_frame import MapFrame
from gui.conclusions_frame import ConclusionsFrame
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def clear_content():

    for widget in content.winfo_children():

        widget.destroy()

def show_heatmaps():

    clear_content()

    frame = HeatmapFrame(
        content
    )

    frame.pack(
        fill="both",
        expand=True
    )
def show_maps():

    clear_content()

    frame = MapFrame(
        content
    )

    frame.pack(
        fill="both",
        expand=True
    )
def show_map():

    clear_content()

    frame = MapFrame(
        content
    )

    frame.pack(
        fill="both",
        expand=True
    )
def show_forecast():

    clear_content()

    frame = ForecastFrame(
        content
    )

    frame.pack(
        fill="both",
        expand=True
    )
def show_model():

    clear_content()

    frame = ModelFrame(
        content
    )

    frame.pack(
        fill="both",
        expand=True
    )   
def show_top10():

    clear_content()

    frame = Top10Frame(
        content
    )

    frame.pack(
        fill="both",
        expand=True
    )
def show_conclusions():

    clear_content()

    frame = ConclusionsFrame(
        content
    )

    frame.pack(
        fill="both",
        expand=True
    )
# =====================
# GŁÓWNE OKNO
# =====================

app = ctk.CTk()

app.title("Analiza OZE i Cen Energii")
app.geometry("1200x800")

# =====================
# LEWY PANEL
# =====================

sidebar = ctk.CTkFrame(
    app,
    width=250
)

sidebar.pack(
    side="left",
    fill="y"
)

# =====================
# GŁÓWNA CZĘŚĆ
# =====================

content = ctk.CTkFrame(app)

content.pack(
    side="right",
    fill="both",
    expand=True
)

# =====================
# TYTUŁ
# =====================

title_label = ctk.CTkLabel(
    content,
    text="Analiza OZE i Cen Energii",
    font=("Arial", 28, "bold")
)

title_label.pack(
    pady=30
)

# =====================
# OPIS
# =====================

description = ctk.CTkLabel(
    content,
    text="""
Aplikacja do analizy:

• udziału OZE
• cen energii
• inflacji
• PKB per capita

Wybierz funkcję z menu po lewej stronie.
"""
)

description.pack()

# =====================
# PRZYCISKI
# =====================

heatmap_btn = ctk.CTkButton(
    sidebar,
    text="Heatmapy",
    command=show_heatmaps
)

heatmap_btn.pack(
    padx=10,
    pady=10,
    fill="x"
)

map_btn = ctk.CTkButton(
    sidebar,
    text="Mapa Europy",
    command=show_map
)

map_btn.pack(
    padx=10,
    pady=10,
    fill="x"
)

forecast_btn = ctk.CTkButton(
    sidebar,
    text="Predykcja",
    command=show_forecast
)

forecast_btn.pack(
    padx=10,
    pady=10,
    fill="x"
)

model_btn = ctk.CTkButton(
    sidebar,
    text="Model",
    command=show_model
)

model_btn.pack(
    padx=10,
    pady=10,
    fill="x"
)

top10_btn = ctk.CTkButton(
    sidebar,
    text="TOP 10 krajów",
    command=show_top10
)

top10_btn.pack(
    padx=10,
    pady=10
)
conclusions_btn = ctk.CTkButton(
    sidebar,
    text="Wnioski",
    command=show_conclusions
)

conclusions_btn.pack(
    padx=10,
    pady=10
)
# =====================
# START APLIKACJI
# =====================

app.mainloop()

from data_loader import load_data

from forecast import predict_country

from excel_export import save_forecast_to_excel

df = load_data()

forecast_df = predict_country(
    "Poland",
    df,
    years=5
)

file_path = save_forecast_to_excel(
    forecast_df,
    "Poland"
)

print(file_path)