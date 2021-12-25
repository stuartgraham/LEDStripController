import board
import neopixel

STRIP1_LED = 150

strip1  = neopixel.NeoPixel(board.D18, 30)

strip1.fill((0, 0, 255))

