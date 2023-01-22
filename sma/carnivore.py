from agent import Agent
from bodyDecomposeur import BodyDecomposeur
from bodyHerbivore import BodyHerbivore


class Carnivore(Agent):
    def __init__(self, body):
        super().__init__(body)
        self.type = "carnivore"

    def filtrePerception(self):
        manger =[]
        for i in self.body.fustrum.perceptionList:
            i.dist = self.body.position.distance_to(i.position)
            if isinstance(i,BodyDecomposeur):
                if(i.status == 'N'):
                    manger.append(i)
            if isinstance(i, BodyHerbivore):
                if(i.status == 'N'):
                    manger.append(i)


        manger.sort(key=lambda x: x.dist, reverse=False)

        return manger, [] , []