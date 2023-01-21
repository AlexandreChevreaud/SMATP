from agent import Agent
from bodyHerbivore import BodyHerbivore


class Decomposeur(Agent):
    def __init__(self, body):
        super().__init__(body)
        self.type = "decomposeur"

    def filtrePerception(self):
        manger = []
        danger = []
        for i in self.body.fustrum.perceptionList:
            i.dist = self.body.position.distance_to(i.position)
            from bodyDecomposeur import BodyDecomposeur
            if hasattr(i, "dateNaissance") and not isinstance(i,BodyDecomposeur):
                if (i.status is 'M'):
                    manger.append(i)
                elif not isinstance(i,BodyDecomposeur) and not isinstance(i,BodyHerbivore):
                    danger.append(i)


        manger.sort(key=lambda x: x.dist, reverse=False)
        danger.sort(key=lambda x: x.dist, reverse=False)
        return manger, danger