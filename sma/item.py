import random

from pygame import Vector2

import core


class Item(object):

    def __init__(self):
        self.position = Vector2(random.uniform(0, core.WINDOW_SIZE[0]), random.uniform(0, core.WINDOW_SIZE[1]))
        self.bodySize = 10
    def show(self):
        pass