from pygame import Vector2
import core
from body import Body
from decomposeur import Decomposeur
from jauge import Jauge


class BodyDecomposeur(Body):
    def __init__(self):
        super().__init__()
        self.jaugeFaim = Jauge(0, 100, 10)
        self.jaugeFatigue = Jauge(0, 100, 60)
        self.jaugeReproduction = Jauge(0, 100, 0)

        self.velocity = Vector2(1.5, 1.5)
        self.acceleration = Vector2(1.5, 1.5)
        self.maxSpeed = 9
        self.maxAcc = 10
        self.dateNaissance = 10
        self.esperanceDeVie = 1000000

    def show(self):
        core.Draw.circle((255,255,255), self.position, self.bodySize)

    def update(self):
        super().update()

        if(self.jaugeReproduction.valeur >= self.jaugeReproduction.max and self.status is not 'M' and self.status is not 'D'):
            self.jaugeReproduction.valeur = self.jaugeReproduction.min
            agent = Decomposeur(BodyDecomposeur())
            agent.body.modificationParametrageNaissance(self.position)
            core.memory("agents").append(agent)