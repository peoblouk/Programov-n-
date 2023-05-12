import pyautogui
import time as t
"""
x = 1
position = pyautogui.position()

while True:
    print(position)
    t.sleep(200)
"""
while True:
    print(pyautogui.displayMousePosition())
    t.sleep(700)
    print(pyautogui.getPointOnLine())