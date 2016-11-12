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

    def __execute(self):
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
            fitnesses = self.population.fitnesses()
            if log:
                logstr = "{}, {}, {}, {}\n".format(self.generation, max(fitnesses), min(fitnesses),
                                                 reduce(lambda x, y: x + y, fitnesses) / len(fitnesses))
                fd.write(logstr)
            self.generation += 1
            if verbose:
                print "generation: {}".format(self.generation)
        if log:
            fd.close()

    def stop(self):
        self._stop = True

    def result(self):
        return self.population.best()
