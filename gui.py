import tkinter as tk
from tkinter import ttk
from functions import *


class mainMenu:
    def __init__(self, root):
        root.title("CV")

        # capture settings
        mainframe = ttk.Frame(root, padding="10")
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.capture_x = tk.StringVar(value="400")
        self.capture_y = tk.StringVar(value="270")
        self.capture_check = tk.BooleanVar()
        self.annotate_check = tk.BooleanVar()
        ttk.Label(mainframe, text="Set capture size in pixels").grid(column=1, row=0, columnspan=2,sticky=tk.W)
        ttk.Label(mainframe, text="Capture Size X:").grid(column=1, row=1, sticky=tk.E)
        ttk.Label(mainframe, text="Capture Size Y:").grid(column=1, row=2, sticky=tk.E)
        self.entry_x = ttk.Entry(mainframe, width=5, textvariable=self.capture_x)
        self.entry_x.grid(column=2, row=1, sticky=(tk.W, tk.E))
        self.entry_y = ttk.Entry(mainframe, width=5, textvariable=self.capture_y)
        self.entry_y.grid(column=2, row=2, sticky=(tk.W, tk.E))

        ttk.Checkbutton(mainframe, text="Capture", variable=self.capture_check, onvalue=True, offvalue=False).grid(column=3, row=1, sticky=tk.W)
        ttk.Checkbutton(mainframe, text="Annotate", variable=self.annotate_check, onvalue=True, offvalue=False).grid(column=3, row=2, sticky=tk.W)

        ttk.Label(mainframe, text="Shift + Left Arrow Key to capture at mouse").grid(column=1, row=3, columnspan=2,sticky=(tk.W, tk.E))

        captureframe = ttk.Frame(root,padding="10")
        captureframe.grid(column=0, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.capture_label = ttk.Label(captureframe, text="No capture yet")
        self.capture_label.pack(expand=True, fill="both", padx=10, pady=10)

        # hotkey logic
        mainframe.bind_all('<Shift-Left>', lambda event: self.hotkey_capture(event))

    def hotkey_capture(self, event):
        if self.capture_check.get():
            screencapture("capturehotkey", *pyautogui.position(), int(self.capture_x.get()), int(self.capture_y.get()))
            self.display_capture()
        if self.annotate_check.get():
            annotatecapture("annotatehotkey", *pyautogui.position(), int(self.capture_x.get()), int(self.capture_y.get()), 0)
        
    def display_capture(self):
        try:
            img = tk.PhotoImage(file="capturehotkey.png")
            self.capture_label.image = img
            self.capture_label.configure(image=img)
            self.capture_label.pack(expand=True, fill="both", padx=10, pady=10)
        except Exception as e:
            pass

root = tk.Tk()
# root.geometry("400x300")
mainMenu(root)
root.mainloop()