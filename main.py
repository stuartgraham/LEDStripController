import time
import random
import board
import neopixel
from dataclasses import dataclass, field
import colour
from itertools import cycle

class LEDStrip(neopixel.NeoPixel):

    def __init__(self, pin=board.D18, n=1, bpp=3 , brightness=0.5, auto_write=False, pixel_order=neopixel.GRB, reverse_order=False):
        super().__init__(pin, n, bpp=3 , brightness=0.3, auto_write=False, pixel_order=neopixel.GRB)
        self.reverse_order = reverse_order
        self.order_reference()

    def order_reference(self):
        self.order_list = list(range(self.n))
        if self.reverse_order:
            self.order_list = self.order_list[::-1]

@dataclass
class LightShow:
    led_strips : list = field(default_factory=list)

    def __post_init__(self):
        for strip in self.led_strips:
            # print(f'pin : {strip.pin}')
            # print(f'len : {len(strip)}')
            # print(f'reverse : {strip.reverse_order}')
            # print(f'order_ref : {strip.order_list}')
            # print(dir(strip))
            pass

        while True:
            self.colours=[colour.DARK_RED, colour.DARK_GREEN]
            self.blinker(20, 3)
            self.colours=[colour.BLACK, colour.CREAM]
            self.blinker(20, 3)
            self.colours=[colour.DARK_RED, colour.DARK_GREEN]
            self.blinker(20, 4)
            self.colours=[colour.BLACK, colour.CREAM]
            self.blinker(20, 4)
            self.colours=[colour.BLUE, colour.YELLOW, colour.GREEN, colour.RED]
            self.random_blink(100, 1)


    def blinker(self, runs, grouping):
        for led_strip in self.led_strips:
            led_strip.fill((colour.BLACK))

        while runs > 0:
            prime_colour = self.colours[0]
            alt_colour = self.colours[0]
            if (runs % 2) == 0:
                prime_colour = self.colours[1]
            else:
                alt_colour = self.colours[1]

            for led_strip in self.led_strips:

                led_list = range(len(led_strip))
                pool = cycle(led_list)

                for i in range(int(len(led_strip) / grouping)):
                    if (i % 2) == 0:
                        for j in range(grouping):
                            led_id = next(pool)
                            led_id = led_strip.order_list[led_id]
                            led_strip[led_id] = prime_colour

                    else:
                        for j in range(grouping):
                            led_id = next(pool)
                            led_id = led_strip.order_list[led_id]
                            led_strip[led_id] = alt_colour

                led_strip.show()
            time.sleep(0.2)
            runs = runs - 1

    def random_blink(self, runs, groupings=1):
        for led_strip in self.led_strips:
            led_strip.fill((colour.BLACK))
        while runs > 0:
            for led_strip in self.led_strips:
                for i in range(len(led_strip)):
                    led_strip[i] = random.choice(self.colours)
                led_strip.show()
            time.sleep(0.2)
            runs = runs - 1


    def barber(self, runs, groups=4):
        pass


left = LEDStrip(board.D18, 150, reverse_order=True)
right = LEDStrip(board.D21, 150, reverse_order=False)

LightShow(led_strips=[left, right])
