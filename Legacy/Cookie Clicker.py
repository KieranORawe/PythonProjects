import pyautogui
import time
import keyboard

pyautogui.PAUSE = 0.001
time.sleep(2)
while True:
    if not keyboard.is_pressed("q"):
        pyautogui.click()
