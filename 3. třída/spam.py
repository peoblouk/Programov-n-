import pyautogui
import time

x = 1404
y = 994
val = 0
10
val = int(input("Enter value of message: "))
print(val)
message = input("Enter your message: ")
print(message)

for i in range(val):
    print(pyautogui.position())
    pyautogui.click(x, y, clicks=3)
    pyautogui.click(x, y, clicks=3)
    pyautogui.typewrite(message)
    pyautogui.hotkey("ENTER")
    pyautogui.typewrite(message)
    pyautogui.hotkey("ENTER")

pyautogui.hotkey("test")


"""
x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        
        
"""
