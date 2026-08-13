import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ControlPanel(ttk.Frame):
    """Panel containing capture settings, path entries, and action buttons."""
    def __init__(self, parent, on_display_click, on_infer_click):
        super().__init__(parent, padding="10")
        
        # Callbacks passed down from main container
        self.on_display_click = on_display_click
        self.on_infer_click = on_infer_click

        # Form variables
        self.capture_x = tk.StringVar(value="400")
        self.capture_y = tk.StringVar(value="270")
        self.capture_check = tk.BooleanVar(value=False)
        self.annotate_check = tk.BooleanVar(value=False)
        self.display_path = tk.StringVar(value="capturehotkey.png")

        self._build_ui()

    def _build_ui(self):
        # Settings Header & Grid Setup
        ttk.Label(self, text="Shift + Left Arrow Key to capture at mouse").grid(column=1, row=0, columnspan=2, sticky=tk.W)
        
        ttk.Label(self, text="Capture Size X:").grid(column=1, row=1, sticky=tk.E)
        ttk.Entry(self, width=5, textvariable=self.capture_x).grid(column=2, row=1, sticky=(tk.W, tk.E))
        
        ttk.Label(self, text="Capture Size Y:").grid(column=1, row=2, sticky=tk.E)
        ttk.Entry(self, width=5, textvariable=self.capture_y).grid(column=2, row=2, sticky=(tk.W, tk.E))
        
        # Checkboxes
        ttk.Checkbutton(self, text="Capture", variable=self.capture_check, onvalue=True, offvalue=False).grid(column=3, row=1, sticky=tk.W)
        ttk.Checkbutton(self, text="Annotate", variable=self.annotate_check, onvalue=True, offvalue=False).grid(column=3, row=2, sticky=tk.W)

        # Path Entry & Action Buttons
        ttk.Label(self, text="Display Path").grid(column=1, row=3, sticky=tk.W)
        ttk.Entry(self, width=15, textvariable=self.display_path).grid(column=2, row=3, sticky=(tk.W, tk.E))
        
        ttk.Button(
            self, 
            text="Display Capture", 
            command=lambda: self.on_display_click(self.display_path.get())
        ).grid(column=3, row=3, sticky=tk.W)
        
        ttk.Button(
            self, 
            text="Run Inference", 
            command=lambda: self.on_infer_click(self.display_path.get())
        ).grid(column=3, row=4, sticky=tk.W)


class DisplayPanel(ttk.Frame):
    """Panel dedicated solely to rendering images."""
    def __init__(self, parent):
        super().__init__(parent, padding="10")
        
        self.capture_label = ttk.Label(self, text="No capture yet")
        self.capture_label.pack(expand=True, fill="both", padx=10, pady=10)

    def render_from_path(self, path: str):
        """Displays a photo file directly."""
        try:
            img = tk.PhotoImage(file=path)
            self._update_label(img)
        except Exception as e:
            print(f"Display Error: {e}")

    def render_pil_image(self, pil_img: Image.Image):
        """Displays a PIL image object (e.g. from YOLO)."""
        try:
            tk_img = ImageTk.PhotoImage(pil_img)
            self._update_label(tk_img)
        except Exception as e:
            print(f"Render Error: {e}")

    def _update_label(self, img):
        self.capture_label.image = img  # Keep reference in memory
        self.capture_label.configure(image=img)