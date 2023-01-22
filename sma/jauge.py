import random


class Jauge(object):
    def __init__(self, min, max, valeur, step):
        self.min  = min;
        self.max  = max;
        self.valeur = valeur;
        self.step = step

    def parametreAleatoireProche(self):
        self.min = 0
        self.max = self.max + random.randint(0,20) - random.randint(0,20)
        self.valeur = self.valeur
        self.step = self.step