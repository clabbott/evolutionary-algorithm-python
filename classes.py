class Environment:
    pop = {}

    def popValues(self):
        return str(self.pop)

    def __init__(self):
        self.pop = {}

    def fillSamples(self,rangeVal):
        self.pop = {}
        for i in range(rangeVal):
            self.pop[i] = i%3
