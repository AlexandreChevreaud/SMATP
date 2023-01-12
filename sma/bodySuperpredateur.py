from pygame import Vector2

import core
from body import Body
from jauge import Jauge
from superpredateur import Superpredateur


class BodySuperpredateur(Body):
    def __init__(self):
        super().__init__()
        self.jaugeFaim = Jauge(0, 80, 70)
        self.jaugeFatigue = Jauge(50, 100, 80)
        self.jaugeReproduction = Jauge(0, 100, 0)

        self.velocity = Vector2(2, 2)
        self.acceleration = Vector2(2, 2)

        self.maxSpeed = 50
        self.maxAcc = 10
        self.dateNaissance = 10
        self.esperanceDeVie = 100

    def show(self):
        core.Draw.circle((255,0,0), self.position, self.bodySize)

    def update(self):
        super().update()

        if(self.jaugeReproduction.valeur >= self.jaugeReproduction.max and self.status is not 'M' and self.status is not 'D'):
            self.jaugeReproduction.valeur = self.jaugeReproduction.min
            agent = Superpredateur(BodySuperpredateur())
            agent.body.modificationParametrageNaissance(self.position)
            core.memory("agents").append(agent)