from interfaces import IEnvironment
from parameters import stopping_criterion
import random


class Environment(IEnvironment):
    def __init__(self):
        pass

    @classmethod
    def goal(cls, population):
        candidate_solution = population.best()
        if candidate_solution.fitness() >= stopping_criterion:
            return True
        return False

    @classmethod
    def fitness(cls, individual):
        individual.fitness = random.randint(0, 100)
        # TODO: implemente Fitness
        pass

    @classmethod
    def evaluate(cls, population):
        [cls.fitness(individual) for individual in population.individuals]
