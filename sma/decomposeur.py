from sma.agent import Agent



class Decomposeur(Agent):
    def __init__(self, body):
        super().__init__(body)

    def filtrePerception(self):
        manger =[]
        for i in self.body.fustrum.perceptionList:
            i.dist = self.body.position.distance_to(i.position)
            if hasattr(i, "dateNaissance"):
                if (i.status is 'M'):
                    manger.append(i)


        manger.sort(key=lambda x: x.dist, reverse=False)

        return manger

    def update(self):
        targets = self.filtrePerception()
        if len(targets) > 0:
            target = targets[0].position - self.body.position
            target.scale_to_length(target.length())
            self.body.acceleration = self.body.acceleration + target