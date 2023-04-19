# read the light sensor

import board, analogio, time

lightsensor = analogio.AnalogIn(board.A8)

while True:
    print("(",lightsensor.value,")")
    time.sleep(0.01)

