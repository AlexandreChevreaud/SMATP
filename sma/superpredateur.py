from sma.agent import Agent
from sma.bodyDecomposeur import BodyDecomposeur


class Superpredateur(Agent):

    def __init__(self, body):
        super().__init__(body)

    def filtrePerception(self):
        decomposeurs =[]
        for i in self.body.fustrum.perceptionList:
            i.dist = self.body.position.distance_to(i.position)
            if isinstance(i,BodyDecomposeur):
                decomposeurs.append(i)


        decomposeurs.sort(key=lambda x: x.dist, reverse=False)

        return decomposeurs

    def update(self):
        targets = self.filtrePerception()
        if len(targets) > 0:
            target = targets[0].position - self.body.position
            target.scale_to_length(target.length())
            self.body.acceleration = self.body.acceleration + target