from pygame import Vector2
import random
from fustrum import Fustrum
import core

from jauge import Jauge


class Body:
    def __init__(self, params):
        self.position = Vector2(random.uniform(0, core.WINDOW_SIZE[0]), random.uniform(0, core.WINDOW_SIZE[1]))

        self.velocity = Vector2(random.uniform(-10, 10), random.uniform(-10,10))
        self.acceleration = Vector2(random.uniform(-10, 10), random.uniform(-10,10))
        self.maxAcc = params[1]
        self.bodySize = 10
        self.maxSpeed = params[0]
        self.velocityMemory = self.velocity
        self.jaugeFaim = Jauge(0,params[2],10,1)
        self.jaugeFatigue = Jauge(0,params[3],10,1)
        self.jaugeReproduction = Jauge(0,params[4],10,1)
        self.dateNaissance = 0
        self.esperanceDeVie = params[5]

        self.fustrum = Fustrum(100, self)
        self.params = params
        self.status = 'N'


    def move(self):
        if self.acceleration.length() > self.maxAcc and self.maxAcc >0:
            self.acceleration.scale_to_length(self.maxAcc)

        self.velocity += self.acceleration
        if self.velocity.length() > self.maxSpeed:
            self.velocity.scale_to_length(self.maxSpeed)

        self.position += self.velocity
        self.acceleration = Vector2(0,0)

    def update(self):
        self.updateValeurVie()
        if self.status == 'N':
            self.move()
        self.edge()

    def updateValeurVie(self):
        if(self.status == 'N'):
            self.jaugeFatigue.valeur += self.jaugeFatigue.step
        else:
            self.jaugeFatigue.valeur -= self.jaugeFatigue.step*3
            if self.jaugeFatigue.valeur <= self.jaugeFatigue.min:
                self.jaugeFatigue.valeur = self.jaugeFatigue.min
                self.status = 'N'
                self.velocity = self.velocityMemory

        self.jaugeFaim.valeur += self.jaugeFaim.step
        self.jaugeReproduction.valeur += self.jaugeReproduction.step
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

    def eat(self):
        self.jaugeFaim.valeur = self.jaugeFaim.min
