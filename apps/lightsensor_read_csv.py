# read the light sensor

import board, analogio, time, neopixel
from adafruit_circuitplayground import cp

lightlist = []

RED    = (255,   0, 0)
YELLOW = (255, 150, 0)
GREEN  = (  0, 255, 0)
BLACK  = (  0,   0, 0)

if cp.switch:
    print("Can't write to USB. Please flip the switch and reconnect.")
else:
    print("All fine. Data will be saved in the data.csv after 10 seconds.")

cp.pixels.fill(RED)
time.sleep(2)
cp.pixels.fill(YELLOW)
time.sleep(2)
cp.pixels.fill(GREEN)
time.sleep(0.5)
cp.pixels.fill(BLACK)

start = time.monotonic()

while start + 11 > time.monotonic():
    light_value = cp.light
    print("(",light_value,")")
    lightlist.append(light_value)
    time.sleep(0.01)

print(len(lightlist))
print(gc.mem_free())

if not cp.switch:
    print("Writing to data.csv")
