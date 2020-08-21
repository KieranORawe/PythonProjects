import pyautogui
from PIL import ImageGrab
import keyboard

game_coords = [1680,416,1681,874] 

def detect_white():
    global game_coords
    image = ImageGrab.grab(bbox=game_coords)
    pixels = image.load()
    __, height = image.size
    white_pixels = []
    for row in range(height):
        pixel = pixels[0, row]
        if pixel == (255, 255, 255):
            return row

while True:
    first_pixel = detect_white()
    if first_pixel != None:
        pyautogui.dragTo(1712,first_pixel+game_coords[1]-50, 0.1)
        
