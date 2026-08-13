from pathlib import Path
from src.cv_pipeline.vision.detector import YoloDetector
from src.cv_pipeline.gui.app import MainMenu

# Resolve paths relative to project root
PROJECT_ROOT = Path(__file__).resolve().parent
MODEL_PATH = PROJECT_ROOT / "src" / "cv_pipeline" / "models" / "yolo26n.pt" 

def main():
    # Initialize your computer vision backend
    print(f"Loading model from: {MODEL_PATH}")
    detector = YoloDetector(model_path=MODEL_PATH)

    # Instantiate the GUI app (it creates its own root window under the hood)
    app = MainMenu(detector=detector)
    
    # (Optional) Set default window geometry
    # app.geometry("600x500")

    # Start the Tkinter mainloop
    app.mainloop()

if __name__ == "__main__":
    main()