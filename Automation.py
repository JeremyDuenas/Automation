import pyautogui
import time

width, height = pyautogui.size()

def get_position_and_color(x,y):
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    image = pyautogui.screenshot()
    pixelColor = image.getpixel((x, y))
    positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
    positionStr += ', ' + str(pixelColor[1]).rjust(3)
    positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')\n'
    return (positionStr)




print('Press Ctrl-C to quit.')
try:
    for x in range(width):
        for y in range(height):
            print(get_position_and_color(x,y))

except KeyboardInterrupt:
    print('Done')
