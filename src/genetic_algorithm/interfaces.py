class IIndividual(object):

    def __init__(self):
        self.moves = []

    def mutate(self):
        pass

    def reproduce(self, other):
        pass


class IPopulation(object):

    def __init__(self):
        self.individuals = []
        self.size = 0

    def init(self):
        pass

    def fitnesses(self):
        pass

    def best(self):
        pass


class IEnvironment(object):

    @classmethod
    def goal(cls, individual):
        pass

    @classmethod
    def fitness(cls, individual):
        pass

    @classmethod
    def evaluate(cls, population):
        pass


class IOperator(object):

    def execute(self, environment, population, generation_number):
        pass
