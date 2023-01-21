import random


class Jauge(object):
    def __init__(self, min, max, valeur, step):
        self.min  = min;
        self.max  = max;
        self.valeur = valeur;
        self.step = step

    def parametreAleatoireProche(self):
        self.min = self.min + random.randint(0,3) - random.randint(0,3)
        self.max = self.max + random.randint(0,3) - random.randint(0,3)
        self.valeur = self.valeur + random.randint(0,3) - random.randint(0,3)
        self.step = self.step