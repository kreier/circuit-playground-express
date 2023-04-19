# read the light sensor

import board, analogio, time

THRESHOLD = 3000
DOT = 0.0019
DASH = 3 * DOT
SPACE = 7 * DOT
average = 0
last_values = []
last_index = 0
old_value = 0
morse = []
letters = {"A":[1,3],"B":[3,1,1,1],"C":[3,1,3,1],"D":[3,1,1],"E":[1],"F":[3,1,1,1],"G":[3,3,1],"H":[1,1,1,1],"I":[1,1],"J":[1,3,3,3],"K":[3,1,3],"L":[1,3,1,1],"M":[3,3],"N":[3,1],"O":[3,3,3],"P":[1,3,3,1],"Q":[3,3,1,3],"R":[1,3,1],"S":[1,1,1],"T":[3],"U":[1,1,3],"V":[1,1,1,3],"W":[1,3,3],"X":[3,1,1,3],"Y":[3,1,3,3],"Z":[3,3,1,1]}
starttime = 0
stoptime = 0

lightsensor = analogio.AnalogIn(board.A8)

# initialize last_values
for i in range(30):
    last_values.append(0)

def get_average(light_raw):
    global last_index
    global last_values
    global average
    last_index += 1
    if last_index >= len(last_values):
        last_index = 0
    last_values[last_index] = light_raw
    average = 0
    for l in last_values:
        average += l
    average /= len(last_values)
    return average

while True:
    light = lightsensor.value
    a = get_average(light)
    if light > average + THRESHOLD:
        light_value = 1
    else:
        light_value = 0
    #print(light_value, end='')
    #print("(", light, ", ", average, ")")
    if light_value != old_value:
        if light_value == 1:
            starttime = time.monotonic()
            # end of letter - 3 dots or 1 dash
            if starttime - stoptime > DASH:
                # decode the letter
                print(morse, end=' ')
                print("A", end='')
                morse = []
        else:
            stoptime = time.monotonic()
            pulsetime = stoptime - starttime
            if pulsetime > DOT:
                if pulsetime > DASH:
                    morse.append(3)
                else:
                    morse.append(1)
    old_value = light_value
    time.sleep(0.001)
