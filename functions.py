from mss import MSS
import mss.tools
import time
import pyautogui
# pyautogui.position() returns mouse pos (x,y) use with screencapture's left/top to cap at mouse pos
# screencapture and annotatecapture needs the x/y positions normalized.



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


