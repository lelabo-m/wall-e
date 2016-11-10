class IIndividual(object):
    def __init__(self):
        self.genes = None #TODO use an other class for genes
        self.score = None

    def mutate(gene):
        pass

class IPopulation(object):
    def __init__(self):
        self.individus = []

class IEnvironment(object):
    def fitness(self, individu):
        pass

class IOperator(object):
    def execute(self, environment, population, generationNumber):
        pass

class AlgoGen(object):
    def __init__(self, population, environment):
        self.population = population
        self.environment = environment
        self.operators = [
            Selection(),
            Crossover(),
            Mutation(),
            Stop()
        ]
        self.generationNumber = 0
        self.stop = False

    def initPopulation(self):
        for individu in self.population.individus:
            individu.score = self.environment.fitness(individu)

    def executeOperator(self):
        for op in self.operators:
            op.execute(self.environment, self.population, self.generationNumber)

    def start(self):
        self.initPopulation()
        while self.stop == False:
            self.executeOperator()
            self.generationNumber += 1

    def stop(self):
        self.stop = True


class Selection(IOperator):
    def execute(self, environment, population, generationNumber):
        #TODO: implemente Selection
        pass

class Mutation(IOperator):
    def execute(self, environment, population, generationNumber):
        #TODO: implemente Mutation
        pass

class Crossover(IOperator):
    def execute(self, environment, population, generationNumber):
        #TODO: implemente Crossover
        pass

class Stop(IOperator):
    def execute(self, environment, population, generationNumber):
        #TODO: implemente Stop
        pass

class Population(IPopulation):
    def __init__(self, pop):
        IPopulation.__init__(self)
        self.individus = []
        #TODO: generate random individu

class Environment(IEnvironment):
    def __init__(self):
        self.goal = None
        #TODO: implemente goal

    def fitness(self, individu):
        #TODO: implemente Fitness
        pass

class Individual(IIndividual):
    def __init__(self):
        IIndividual.__init__(self)
        self.genes = None #TODO use an other class for genes
        self.score = None




algo = AlgoGen(Environment(), Population(400))

algo.start()
