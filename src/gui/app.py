import customtkinter as ctk
from gui.sidebar import Sidebar
from gui.home_frame import HomeFrame
from gui.heatmap_frame import HeatmapFrame
from gui.map_frame import MapFrame
from gui.forecast_frame import ForecastFrame
from gui.model_frame import ModelFrame
from gui.top10_frame import Top10Frame
from gui.conclusions_frame import ConclusionsFrame
from gui.styles import *


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class OZEApplication(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("Analiza OZE i Cen Energii")

        self.geometry("1300x850")

        # =====================
        # SIDEBAR
        # =====================

        self.sidebar = Sidebar(
            self,
            self
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )
        # =====================
        # CONTENT
        # =====================

        self.content = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color=APP_BACKGROUND
        )

        self.content.pack(
            side="right",
            fill="both",
            expand=True
        )

        # Ekran startowy

        self.show_home()

    # =================================

    def clear_content(self):

        for widget in self.content.winfo_children():

            widget.destroy()

    # =================================
    def show_frame(self, frame_class):

        self.clear_content()

        frame = frame_class(
            self.content
        )

        frame.pack(
            fill="both",
            expand=True
        )   
    def show_home(self):

        self.show_frame(HomeFrame)

    # =================================

    def show_heatmaps(self):

        self.show_frame(
            HeatmapFrame
        )

    # =================================

    def show_map(self):

        self.show_frame(
            MapFrame
        )
    # =================================

    def show_forecast(self):

        self.show_frame(
            ForecastFrame
        )

    # =================================

    def show_model(self):

        self.show_frame(
            ModelFrame
        )

    # =================================

    def show_top10(self):

        self.show_frame(
            Top10Frame
        )

    # =================================


    def show_conclusions(self):

        self.show_frame(
            ConclusionsFrame
        )