from pygame import Vector2
import random
from fustrum import Fustrum
import core
import datetime

from sma.jauge import Jauge


class Body:
    def __init__(self):
        self.position = Vector2(random.uniform(0, core.WINDOW_SIZE[0]), random.uniform(0, core.WINDOW_SIZE[1]))
        self.velocity = Vector2(random.uniform(-10, 10), random.uniform(-10,10))
        self.acceleration = Vector2(random.uniform(-10, 10), random.uniform(-10,10))
        self.maxAcc = 10
        self.bodySize = 10
        self.maxSpeed = 3

        self.jaugeFaim = Jauge(0,100,50)
        self.jaugeFatigue = Jauge(0,100,50)
        self.jaugeReproduction = Jauge(0,100,50)

        self.dateNaissance = datetime.datetime.now()
        self.esperanceDeVie = 100

        self.fustrum = Fustrum(300, self)

        self.status = 'N'


    def move(self):
        if self.acceleration.length() > self.maxAcc:
            self.acceleration.scale_to_length(self.maxAcc)

        self.velocity += self.acceleration
        if self.velocity.length() > self.maxSpeed:
            self.velocity.scale_to_length(self.maxSpeed)

        self.position += self.velocity
        self.acceleration = Vector2(0,0)

    def update(self):
        self.updateValeurVie()
        self.move()
        self.edge()

    def updateValeurVie(self):
        self.jaugeFatigue.valeur += 1
        self.jaugeFaim.valeur += 1
        self.jaugeReproduction.valeur += 1
        self.dateNaissance += 1

        if (self.dateNaissance >= self.esperanceDeVie):
            self.velocity = Vector2(0, 0)
            self.status = 'M'
        if (self.jaugeFaim.valeur >= self.jaugeFaim.max):
            self.velocity = Vector2(0, 0)
            self.status = 'M'
        if(self.jaugeFatigue.valeur >= self.jaugeFatigue.max):
            self.velocity = Vector2(0, 0)
            self.status = 'D'

    def show(self):
        pass

    def edge(self):
        if self.position.x <= self.bodySize:
            self.velocity.x *= -1
        if self.position.x + self.bodySize >= core.WINDOW_SIZE[0]:
            self.velocity.x *= -1
        if self.position.y <= self.bodySize:
            self.velocity.y *= -1
        if self.position.y + self.bodySize >= core.WINDOW_SIZE[1]:
            self.velocity.y *= -1


    def modificationParametrageNaissance(self, position):
        self.jaugeReproduction.parametreAleatoireProche()
        self.jaugeFatigue.parametreAleatoireProche()
        self.jaugeFaim.parametreAleatoireProche()
        self.esperanceDeVie = self.esperanceDeVie + random.randint(0,3) - random.randint(0,3)
        self.maxSpeed = self.maxSpeed + random.randint(0,3) - random.randint(0,3)
        self.maxAcc = self.maxAcc + random.randint(0,3) - random.randint(0,3)
        self.velocity.x = self.velocity.x + random.randint(0,2) - random.randint(0,2)
        self.acceleration.x = self.acceleration.x + random.randint(0,2) - random.randint(0,2)
        self.velocity.y = self.velocity.y + random.randint(0,2) - random.randint(0,2)
        self.acceleration.y = self.acceleration.y + random.randint(0,2) - random.randint(0,2)
        self.position =Vector2(position.x,position.y)
