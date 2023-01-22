import random

from pygame import Vector2
class Agent(object):
    def __init__(self, body):
        self.body = body
        self.uuid = random.randint(100000, 999999999)
        self.type = ""
        self.coefDanger = 100
        self.coefManger = 0.01
        self.coefSymbiose = 0.01

    def show(self):
        self.body.show()

    def update(self):
        targets,dangers,symbiose = self.filtrePerception()
        if len(targets) > 0:
            target = targets[0].position - self.body.position
            if (target.length() != 0):
                target.scale_to_length(target.length() * self.coefManger)
            self.body.acceleration = self.body.acceleration + target

        if len(dangers)>0:
            target = self.body.position - dangers[0].position
            target.scale_to_length(1 / target.length() ** 2)
            target.scale_to_length(target.length() * (self.coefDanger + self.body.bodySize))
            self.body.acceleration = self.body.acceleration + target

        if len(symbiose) > 0:
            target = symbiose[0].position - self.body.position
            if (target.length() != 0):
                target.scale_to_length(target.length() * self.coefSymbiose)
            self.body.acceleration = self.body.acceleration + target

    def filtrePerception(self):
        return [], [], []

    def getValeurGenetique(self):
        return (self.body.maxSpeed) * (self.body.maxAcc) * (self.body.jaugeFaim.max) * (self.body.jaugeFatigue.max) * (self.body.esperanceDeVie) * (self.body.jaugeReproduction.max)