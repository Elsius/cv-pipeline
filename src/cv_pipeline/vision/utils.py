from mss import MSS
import mss.tools
import time
import pyautogui
import cv2
from PIL import Image, ImageTk
from ultralytics import YOLO

# pyautogui.position() returns mouse pos (x,y) use with screencapture's left/top to cap at mouse pos
# capture/annotate will offset mouse pos as center of target


def screencapture(output = "capture", left=0, top=0, width=1920, height=1080):
    # offset to center
    monitor = {"top": (top - (height // 2)), "left": (left - (width // 2)), "width": width, "height": height}
    img_output = f'{output}.png'
    with MSS() as sct:
        sct_image = sct.grab(monitor)
        mss.tools.to_png(sct_image.rgb, sct_image.size, output = img_output)

def annotatecapture(output = "capture", left = 0, top = 0, width = 1920, height = 1090, class_id = 0):
    txt_output = f'{output}.txt'
    # offset to center
    left = left - (width // 2)
    top = top - (height // 2)

    with open(txt_output, 'a') as f:
        f.write(f"{class_id} {left} {top} {width} {height}\n")

def convert_yolo_to_pil(result): # Converts result > numpy array > PIL Image
    annotated_frame = result[0].plot()
    annotated_frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(annotated_frame_rgb)
    return pil_img
