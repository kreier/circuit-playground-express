# Start menu with 10 neopixel and button A (select) and B (confirm)
# v0.1 2023-04-07

import time, board, neopixel
from digitalio import DigitalInOut, Direction, Pull

select = DigitalInOut(board.BUTTON_A)
select.direction = Direction.INPUT
confirm = DigitalInOut(board.BUTTON_B)
confirm.direction = Direction.INPUT

num_pixels = 10
neo = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=0.1, auto_write=False)

selection = 9

for i in range(num_pixels):
    neo[i] = (0, 255, 0)
neo.show()

while not confirm.value:
    while not select.value:
        neo[selection] = (255, 0, 0)
        neo.show()
        #time.sleep(0.01)
    neo[selection] = (0, 255, 0)
    selection -= 1
    if selection < 0:
        selection = 9
    print("you select ", selection)
    neo[selection] = (255, 0, 0)
    #time.sleep(0.02)

print("You selected option ", selection)
