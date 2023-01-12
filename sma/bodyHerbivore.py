from pygame import Vector2

import core
from body import Body
from jauge import Jauge
from herbivore import Herbivore


class BodyHerbivore(Body):
    def __init__(self):
        super().__init__()
        self.jaugeFaim = Jauge(0, 200, 20)
        self.jaugeFatigue = Jauge(0, 150, 30)
        self.jaugeReproduction = Jauge(0, 100, 0)

        self.velocity = Vector2(2, 2)
        self.acceleration = Vector2(2, 2)
        self.maxSpeed = 7
        self.maxAcc = 7
        self.dateNaissance = 10
        self.esperanceDeVie = 100


    def show(self):
        core.Draw.circle((0,255,0), self.position, self.bodySize)

    def update(self):
        super().update()

        if(self.jaugeReproduction.valeur >= self.jaugeReproduction.max and self.status is not 'M' and self.status is not 'D'):
            self.jaugeReproduction.valeur = self.jaugeReproduction.min
            agent = Herbivore(BodyHerbivore())
            agent.body.modificationParametrageNaissance(self.position)
            core.memory("agents").append(agent)
