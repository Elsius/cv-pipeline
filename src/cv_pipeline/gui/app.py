import tkinter as tk
import pyautogui
# Assume screencapture and annotatecapture are in your vision utils
from src.cv_pipeline.vision.utils import screencapture, annotatecapture
from src.cv_pipeline.vision.detector import YoloDetector
from src.cv_pipeline.gui.components.panels import ControlPanel, DisplayPanel

class MainMenu(tk.Tk):
    def __init__(self, detector: YoloDetector):
        super().__init__()
        self.title("CV Pipeline")
        self.detector = detector

        # 1. Instantiate modular components
        self.control_panel = ControlPanel(
            parent=self, 
            on_display_click=self.handle_display, 
            on_infer_click=self.handle_inference
        )
        self.display_panel = DisplayPanel(parent=self)

        # 2. Arrange panels on grid
        self.control_panel.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.display_panel.grid(column=0, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))

        # 3. Bind global hotkey
        self.bind_all('<Shift-Left>', self.hotkey_capture)

    # Event / Action Handlers
    def handle_display(self, path: str):
        self.display_panel.render_from_path(path)

    def handle_inference(self, path: str):
        try:
            pil_img = self.detector.run_inference(path)
            self.display_panel.render_pil_image(pil_img)
        except Exception as e:
            print(f"Inference Error: {e}")

    def hotkey_capture(self, event):
        x_size = int(self.control_panel.capture_x.get())
        y_size = int(self.control_panel.capture_y.get())
        pos = pyautogui.position()

        if self.control_panel.capture_check.get():
            screencapture("capturehotkey", *pos, x_size, y_size)
            self.display_panel.render_from_path("capturehotkey.png")
            
        if self.control_panel.annotate_check.get():
            annotatecapture("annotatehotkey", *pos, x_size, y_size, 0)