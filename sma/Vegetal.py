import core
from item import Item


class Vegetal(Item):

    def __init__(self):
        super().__init__()
        self.bodySize = 10

    def show(self):
        core.Draw.circle((238, 130, 238), self.position, self.bodySize)
