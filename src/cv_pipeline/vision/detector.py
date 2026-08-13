from pathlib import Path
from PIL import Image
from ultralytics import YOLO

class YoloDetector:
    def __init__(self, model_path: Path):
        self.model = YOLO(str(model_path))

    def run_inference(self, image_path: str) -> Image.Image:
        """Runs YOLO on an image file and returns a PIL Image."""
        results = self.model(image_path, save=False)
        
        # Plot returns a BGR numpy array; convert to RGB for PIL
        res_plotted = results[0].plot()
        pil_img = Image.fromarray(res_plotted[..., ::-1])
        return pil_img