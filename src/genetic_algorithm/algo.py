from operators import *


class GeneticAlgorithm(object):
    def __init__(self, population, environment):
        self.population = population
        self.environment = environment
        self.operators = [
            Selection(),
            Crossover(),
            Mutation(),
            Stop()
        ]
        self.generation = 0
        self._stop = False
        self.fitnesses = None

    def __execute(self):
        self.environment.evaluate(self.population)
        self.fitnesses = self.population.fitnesses()
        for op in self.operators:
            self._stop = op.execute(self.environment, self.population, self.generation)

    def start(self, log=True, path="genetic-algo.log", verbose=False):
        self.population.init()
        fd = None
        if log:
            fd = open(path, "w")
            fd.write("generation_number, max, min, avg\n")
        while self._stop is False:
            self.__execute()
            logstr = "{}, {}, {}, {}\n".format(self.generation, max(self.fitnesses), min(self.fitnesses),
                                               reduce(lambda x, y: x + y, self.fitnesses) / len(self.fitnesses))
            if log:
                fd.write(logstr)
            self.generation += 1
            if verbose:
                print logstr
                print self.population.best().moves
                print "generation: {}".format(self.generation)
        if log:
            fd.close()

    def stop(self):
        self._stop = True

    def result(self):
        return self.population.best()
