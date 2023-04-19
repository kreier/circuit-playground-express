# Save 10 seconds of the light sensor - with traffic light indicator

import board, analogio, time, neopixel

lightsensor = analogio.AnalogIn(board.A8)
neo = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.05, auto_write=False)
data_light = []

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

start = time.monotonic()

while start + 1 > time.monotonic():
    light_int16 = lightsensor.value
    print("(",light_int16,")")
    data_light.append(light_int16)
    time.sleep(0.01)

print("I collected a lot of data.")
print(len(data_light))
print(data_light)

with open("/tmp.txt", "a") as fp:
    fp.write("Hello world")
