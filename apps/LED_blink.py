import digitalio
import board
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True
print("The LED is now on!")
time.sleep(5)
led.value = False
time.sleep(1)
led.value = True
time.sleep(1)
led.value = False
time.sleep(1)
led.value = True
time.sleep(1)
led.value = False
time.sleep(1)
led.value = True
time.sleep(1)
led.value = False
time.sleep(1)
led.value = True
time.sleep(1)
led.value = False
time.sleep(1)
led.value = True
time.sleep(1)

