import random

from pygame import Vector2

import core
from body import Body
from jauge import Jauge
from superpredateur import Superpredateur


class BodySuperpredateur(Body):
    def __init__(self,params):
        super().__init__(params)

        self.velocity = Vector2(random.randint(-self.maxSpeed,self.maxSpeed), random.randint(-self.maxSpeed,self.maxSpeed))
        self.acceleration = Vector2(3, 3)
        self.dateNaissance = 10
        self.velocityMemory = self.velocity

    def show(self):
        core.Draw.circle((255,0,0), self.position, self.bodySize)

    def update(self):
        super().update()
        if(self.jaugeReproduction.valeur >= self.jaugeReproduction.max and self.status != 'M' and self.status != 'D'):
            self.jaugeReproduction.valeur = self.jaugeReproduction.min
            agent = Superpredateur(BodySuperpredateur(self.params))
            agent.body.modificationParametrageNaissance(self.position)
            core.memory("agents").append(agent)