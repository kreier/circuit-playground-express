# use the neopixel as Morse output

import board, time
from adafruit_circuitplayground import cp

message = "ADVANCED AUTOMATION IS GREAT "
DOT = 0.02
DASH = 3
SPACE = 7
WHITE  = (255, 255, 255)
BLACK  = (  0,   0,   0)
letters = {"A":[1,3],"B":[3,1,1,1],"C":[3,1,3,1],"D":[3,1,1],"E":[1],"F":[3,1,1,1],"G":[3,3,1],"H":[1,1,1,1],"I":[1,1],"J":[1,3,3,3],"K":[3,1,3],"L":[1,3,1,1],"M":[3,3],"N":[3,1],"O":[3,3,3],"P":[1,3,3,1],"Q":[3,3,1,3],"R":[1,3,1],"S":[1,1,1],"T":[3],"U":[1,1,3],"V":[1,1,1,3],"W":[1,3,3],"X":[3,1,1,3],"Y":[3,1,3,3],"Z":[3,3,1,1]}

while True:
    for i in range(len(message)):
        letter = message[i:i+1]
        print(letter, end='')
        try:
            morse = letters[letter]
        except:
            morse = [7]
        #print(morse, end='')
        if morse == [7]:
            time.sleep(DOT * SPACE)
        else:
            for a in morse:
                cp.pixels.fill(WHITE)
                time.sleep(a * DOT)
                cp.pixels.fill(BLACK)
                time.sleep(DOT)
            time.sleep(DOT * DASH)
    print(' ')
