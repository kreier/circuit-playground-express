# indicate reading of the light sensor with neopixel

import board, analogio, time, neopixel

lightsensor = analogio.AnalogIn(board.A8)

neo = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.05, auto_write=False)

RED    = (255,   0, 0)
YELLOW = (255, 150, 0)
GREEN  = (  0, 255, 0)
BLACK  = (  0,   0, 0)

neo.fill(RED)
neo.show()
time.sleep(2)
neo.fill(YELLOW)
neo.show()
time.sleep(2)
neo.fill(GREEN)
neo.show()
time.sleep(0.5)
neo.fill(BLACK)
neo.show()

while True:
    print("(",lightsensor.value,")")
    time.sleep(0.01)
