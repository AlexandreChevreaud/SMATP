from Vegetal import Vegetal
from agent import Agent


class Herbivore(Agent):
    def __init__(self, body):
        super().__init__(body)
        self.type = "herbivore"

    def filtrePerception(self):
        manger  = []
        danger  = []
        symbiose = []
        for i in self.body.fustrum.perceptionList:
            i.dist = self.body.position.distance_to(i.position)
            from bodyHerbivore import BodyHerbivore
            from bodyDecomposeur import BodyDecomposeur
            from bodySuperpredateur import BodySuperpredateur
            if isinstance(i,Vegetal):
                manger.append(i)
            elif not isinstance(i, BodyDecomposeur) and not isinstance(i, BodyHerbivore):
                if (i.status is 'N'):
                    danger.append(i)
            if isinstance(i, BodySuperpredateur):
                if (i.status is 'N'):
                    symbiose.append(i)

        manger.sort(key=lambda x: x.dist, reverse=False)
        danger.sort(key=lambda x: x.dist, reverse=False)
        symbiose.sort(key=lambda x: x.dist, reverse=False)
        return manger, danger, symbiose
