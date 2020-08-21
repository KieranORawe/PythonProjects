import pyautogui
import keyboard

while True:
    if not keyboard.is_pressed("q"):
        pyautogui.keyDown("w")
        pyautogui.mouseDown()
    else:
        break
