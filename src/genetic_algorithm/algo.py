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

    def start(self):
        self.population.init()
        print "generation_number, max, min, avg"
        while self._stop is False:
            self.__execute()
            fitnesses = self.environment(self.population)
            print "{}, {}, {}, {}".format(self.generation, max(fitnesses), min(fitnesses),
                                          reduce(lambda x, y: x + y, fitnesses) / len(fitnesses))
            self.generation += 1

    def stop(self):
        self._stop = True

    def result(self):
        return self.population.best()
