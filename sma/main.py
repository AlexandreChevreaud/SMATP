from collections import Counter

import core
from sma.bodyCarnivore import BodyCarnivore
from sma.bodyDecomposeur import BodyDecomposeur
from sma.bodyHerbivore import BodyHerbivore
from sma.bodySuperpredateur import BodySuperpredateur
from sma.carnivore import Carnivore
from sma.decomposeur import Decomposeur
from sma.herbivore import Herbivore
from sma.superpredateur import Superpredateur


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 800]

    core.memory("agents", [])
    core.memory("nbAgents", 40)
    core.memory("nbCarnivores", 3)
    core.memory("nbHerbivores", 3)
    core.memory("nbSuperpredateurs", 3)
    core.memory("nbDecomposeurs", 30)
    core.memory("item", [])
    for i in range(0, core.memory("nbCarnivores")):
        core.memory("agents").append(Carnivore(BodyCarnivore()))

    for i in range(0, core.memory("nbHerbivores")):
        core.memory("agents").append(Herbivore(BodyHerbivore()))

    for i in range(0, core.memory("nbSuperpredateurs")):
        core.memory("agents").append(Superpredateur(BodySuperpredateur()))

    for i in range(0, core.memory("nbDecomposeurs")):
        core.memory("agents").append(Decomposeur(BodyDecomposeur()))

    print("Setup END-----------")


def computePerception(agent):
        agent.body.fustrum.perceptionList=[]
        for b in core.memory('agents'):
            if agent.uuid!=b.uuid:
                if agent.body.fustrum.inside(b.body):
                    agent.body.fustrum.perceptionList.append(b.body)


def computeDecision(agent):
    agent.update()


def applyDecision(agent):
    agent.body.update()

def updateEnv():
    for a in core.memory("agents"):
        for c in core.memory('agents'):
            if c.uuid != a.uuid:
                if a.body.position.distance_to(c.body.position) <= a.body.bodySize+c.body.bodySize:
                    if(isinstance(a,Carnivore) and isinstance(c,Decomposeur)):
                        core.memory("agents").remove(c)
                    if (isinstance(a, Superpredateur) and isinstance(c, Decomposeur)):
                        core.memory("agents").remove(c)
                    if (isinstance(a, Decomposeur) and hasattr(c,"dateNaissance")):
                        if(c.body.status is 'M'):
                            core.memory("agents").remove(c)


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

    # Compter le nombre d'agents ayant chaque statut
    status_counts = Counter(agent.type for agent in agents)
    print('-----------------------------------------------------------------')
    for status, count in status_counts.items():

        print("Il y a {} agents ayant un statut '{}' ce qui représente {}%".format(count, status,(count/len(agents))*100))
    print('-----------------------------------------------------------------')

core.main(setup, run)
