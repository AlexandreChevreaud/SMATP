import random
from collections import Counter
import matplotlib.pyplot as plt
from pygame import Vector2

import core
from Vegetal import Vegetal
from bodyCarnivore import BodyCarnivore
from bodyDecomposeur import BodyDecomposeur
from bodyHerbivore import BodyHerbivore
from bodySuperpredateur import BodySuperpredateur
from carnivore import Carnivore
from decomposeur import Decomposeur
from herbivore import Herbivore
from superpredateur import Superpredateur
import json

printValeur = False

def randomValues(parametre):
    vitesse = random.randint(int(parametre['vitesseMax'][0]),int(parametre['vitesseMax'][1]))
    acceleration = random.randint(int(parametre['accelerationMax'][0]),int(parametre['accelerationMax'][1]))
    faim = random.randint(int(parametre['MaxFaim'][0]),int(parametre['MaxFaim'][1]))
    fatigue = random.randint(int(parametre['MaxFatique'][0]),int(parametre['MaxFatique'][1]))
    reproduction = random.randint(int(parametre['MaxRepoduction'][0]),int(parametre['MaxRepoduction'][1]))
    esperanceVie = random.randint(int(parametre['esperanceDeVie'][0]),int(parametre['esperanceDeVie'][1]))

    return vitesse, acceleration,faim, fatigue, reproduction, esperanceVie
def load(path):
    with open('scenario.json', 'r') as json_file:
        data = json.load(json_file)

        core.memory("agents", [])
        core.memory("item", [])
        core.memory("nbCarnivores", data['Carnivore']['nb'])
        core.memory("nbHerbivores", data['Herbivore']['nb'])
        core.memory("nbSuperpredateurs", data['SuperPredateur']['nb'])
        core.memory("nbDecomposeurs", data['Decomposeur']['nb'])
        core.memory("nbVegetaux", data['Vegetaux']['nb'])

        paramsCarnivore = randomValues(data['Carnivore']['parametres'])
        paramsHerbivore = randomValues(data['Herbivore']['parametres'])
        paramsSuperPredateur = randomValues(data['SuperPredateur']['parametres'])
        paramsDecomposeur= randomValues(data['Decomposeur']['parametres'])
        core.duree = data['duréeSimu']

        for i in range(0, core.memory("nbCarnivores")):
            core.memory("agents").append(Carnivore(BodyCarnivore(paramsCarnivore)))

        for i in range(0, core.memory("nbHerbivores")):
            core.memory("agents").append(Herbivore(BodyHerbivore(paramsHerbivore)))

        for i in range(0, core.memory("nbSuperpredateurs")):
            core.memory("agents").append(Superpredateur(BodySuperpredateur(paramsSuperPredateur)))

        for i in range(0, core.memory("nbDecomposeurs")):
            core.memory("agents").append(Decomposeur(BodyDecomposeur(paramsDecomposeur)))

        for i in range(0, core.memory("nbVegetaux")):
            core.memory("item").append(Vegetal())

def graphique():
    plt.cla()
    agents = core.memory("agents")
    listNombre = [0,0,0,0,0]
    listStatus = ['Herbivores','Carnivores','Superpredateurs','Decomposeurs','Vegetaux']
    for agent in agents:
        if agent.body.status != 'M':
            if isinstance(agent,Herbivore):
                listNombre[0] += 1
            if isinstance(agent,Carnivore):
                listNombre[1] += 1
            if isinstance(agent,Superpredateur):
                listNombre[2] += 1
            if isinstance(agent,Decomposeur):
                listNombre[3] += 1

    for item in core.memory("item"):
        if isinstance(item,Vegetal):
            listNombre[4] += 1


    plt.bar(listStatus, listNombre)
    plt.ion()
    plt.draw()
    plt.show()
    plt.pause(0.000001)

def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 800]

    load("scenario.json")

    print("Setup END-----------")


def computePerception(agent):
        agent.body.fustrum.perceptionList=[]
        for b in core.memory('agents'):
            if agent.uuid!=b.uuid:
                if agent.body.fustrum.inside(b.body):
                    agent.body.fustrum.perceptionList.append(b.body)
        for i in core.memory('item'):
            if agent.body.fustrum.inside(i):
                agent.body.fustrum.perceptionList.append(i)


def computeDecision(agent):
    agent.update()


def applyDecision(agent):
    agent.body.update()

def updateEnv():
    for a in core.memory("agents"):
        for c in core.memory('agents'):
            if c.uuid != a.uuid:
                if a.body.position.distance_to(c.body.position) <= a.body.bodySize+c.body.bodySize:

                    if(isinstance(a,Carnivore) and (isinstance(c,Decomposeur) or isinstance(c,Herbivore))):
                        if(a.body.status == 'N'):
                            core.memory("agents").remove(c)
                            a.body.eat()
                    if (isinstance(a, Superpredateur) and (isinstance(c, Decomposeur) or isinstance(c,Herbivore) or isinstance(c,Carnivore))):
                        if (a.body.status == 'N'):
                            core.memory("agents").remove(c)
                            a.body.eat()
                    if (isinstance(a, Decomposeur) and hasattr(c.body,"dateNaissance")):
                        if(c.body.status is 'M'):
                            core.memory("agents").remove(c)
                            a.body.eat()
                            vegetal = Vegetal()
                            vegetal.position = Vector2(a.body.position.x,a.body.position.y)
                            core.memory("item").append(vegetal)


        for i in core.memory('item'):
            if a.body.position.distance_to(i.position) <= a.body.bodySize + i.bodySize:
                if (isinstance(a, Herbivore) and isinstance(i, Vegetal)):
                    core.memory("item").remove(i)
                    a.body.eat()

def run():
    core.cleanScreen()
    agents = core.memory("agents")


    #Display
    for agent in agents:
        agent.show()

    for item in core.memory("item"):
        item.show()

    for agent in core.memory("agents"):
        computePerception(agent)

    for agent in core.memory("agents"):
        computeDecision(agent)

    for agent in core.memory("agents"):
        applyDecision(agent)

    updateEnv()
    if (printValeur == True):
        # Compter le nombre d'agents ayant chaque statut
        status_counts = Counter(agent.type for agent in agents)
        print('-----------------------------------------------------------------')
        for status, count in status_counts.items():

            print("Il y a {} agents ayant un statut '{}' ce qui représente {}%".format(count, status,(count/len(agents))*100))
        print('-----------------------------------------------------------------')

    graphique()
core.main(setup, run)
