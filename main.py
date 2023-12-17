import time
import random

import board
import neopixel
from dataclasses import dataclass, field
import colour
from itertools import cycle
from datetime import datetime

MONTH = datetime.now().month
DAY = datetime.now().day

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
        while True:
            # HALLOWEEN
            # HALLOWEEN_DAYS = [30,31]
            # if MONTH == 10 and DAY in HALLOWEEN_DAYS:
            #     self.halloween()
            #     print('Its Halloween')
            # CHRISTMAS
            # christmas_day_window = [1,26]
            # christmas_day_window_open = False
            # if christmas_day_window[0] < DAY and DAY < christmas_day_window[1]: 
            #     christmas_day_window_open = True
            # if MONTH == 12 and christmas_day_window_open:
            #     self.christmas()
            #     print('Its Christmas')
            #RANGERS
            self.rangers()

    def halloween(self):
        self.colours=[colour.DARK_ORANGE, colour.DARK_GREEN]
        self.blinker(20, 3)
        self.colours=[colour.DARK_ORANGE, colour.BLACK]
        self.blinker(20, 10)


    def christmas(self):
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

    def rangers(self):
        self.colours=[colour.BLUE, colour.WHITE, colour.DARK_RED, ]
        self.blinker(20, 3)

    def blank_lights(self):
        for led_strip in self.led_strips:
            led_strip.fill((colour.BLACK))

    def blinker(self, runs, grouping):
        self.blank_lights()

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
                        for _ in range(grouping):
                            led_id = next(pool)
                            led_id = led_strip.order_list[led_id]
                            led_strip[led_id] = prime_colour

                    else:
                        for _ in range(grouping):
                            led_id = next(pool)
                            led_id = led_strip.order_list[led_id]
                            led_strip[led_id] = alt_colour

                led_strip.show()
            #time.sleep(0.2)
            time.sleep(1)
            runs = runs - 1

    def random_blink(self, runs, groupings=1):
        self.blank_lights()

        while runs > 0:
            for led_strip in self.led_strips:
                for i in range(len(led_strip)):
                    led_strip[i] = random.choice(self.colours)
                led_strip.show()
            time.sleep(0.2)
            runs = runs - 1


left = LEDStrip(board.D18, 150, reverse_order=True)
right = LEDStrip(board.D21, 150, reverse_order=False)

LightShow(led_strips=[left, right])
