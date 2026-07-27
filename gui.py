import tkinter as tk
from tkinter import ttk
from functions import *


class mainMenu:
    def __init__(self, root):
        root.title("CV")
        mainframe = ttk.Frame(root, padding="10")
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))


        ttk.Button(mainframe, text="Capture", command=self.capture_button).grid(column=2, row=3, sticky=tk.W)
        ttk.Button(mainframe, text="Annotate", command=self.annotate_button).grid(column=3, row=3, sticky=tk.W)
    def capture_button(self):
        screencapture("capturebutton", *pyautogui.position(), 500, 500)

    def annotate_button(self):
        annotatecapture("annotatebutton", *pyautogui.position(), 500, 500, 0)

root = tk.Tk()
root.geometry("400x300")
mainMenu(root)
root.mainloop()