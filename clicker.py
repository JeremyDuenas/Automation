import pyautogui
import time
x = 1365
y = 928
try:
    while True:
        time.sleep(60)
        pyautogui.click(x,y)

except KeyboardInterrupt:
    print('Done')
