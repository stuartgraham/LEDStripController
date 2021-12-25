


import board
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy
import time
num_leds = 16
i = 0
pixels = neopixel.NeoPixel(board.A0, num_leds, brightness=1.0,
                            auto_write=False)
loopmillis = 0

patterndown = [0, .07, .13, .2, .27, .33, .4, .47, .53, .6, .67, .73, .8, .87, .93, 1.0]
patternup = [1.0, .93, .87, .8, .73, .67, .6, .53, .47, .4, .33, .27, .2, .13, .07, 0]
i = 0
index = 0
count = 0
black = fancy.CRGB(0.0, 0.0, 0.0)

# pixelscopy[] = pixels.copy[]
def up():
    initial = time.monotonic()
    index = 0
    count = 0
    while count <= len(pixels):
        now = time.monotonic()
        if now - initial > .01:
            if index == 0:
                temp = patternup[index]
            if index < 15:
                patternup[index] = patternup[index+1]
            if index == 15:
                patternup[index] = temp
            color = fancy.CHSV(0, 1.0,  patternup[index])
            levels = (.75, .8, .60)
            gammas = (2.9, 2.5, 2.4)
            color = fancy.gamma_adjust(color, brightness=levels, gamma_value=gammas)
            pixels[index] = color.pack()
            pixels.show()
            # print(count)
            #print(pattern[index], index)
            index = index + 1
            if index> 15:
                index = 0
                initial = now
                count = count + 1
            if count == len(pixels):
                pixels.fill(black)
                pixels.show()

def down():
    initial = time.monotonic()
    index = 15
    count = 0

    while count <= len(pixels):
        now = time.monotonic()
        if now - initial > .01:
            if index == 15:
                temp = patterndown[index]
            if index > 0:
                patterndown[index] = patterndown[index-1]
            if index == 0:
                patterndown[index] = temp
            color = fancy.CHSV(0, 1.0,  patterndown[index])
            levels = (.75, .8, .60)
            gammas = (2.9, 2.5, 2.4)
            color = fancy.gamma_adjust(color, brightness=levels, gamma_value=gammas)
            pixels[index] = color.pack()
            pixels.show()
            index = index - 1
            if index < 0:
                index = 15
                initial = now
                count = count + 1

while True:
    up()
    down()