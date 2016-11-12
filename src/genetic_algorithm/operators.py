from interfaces import *
from parameters import *
import random
from utils import rand_probability


class Selection(IOperator):

    def execute(self, environment, population, generation):
        environment.evaluate(population)
        best_solution = population.best()
        fitnesses = population.fitnesses()
        total_fitness = sum(fitnesses)
        rel_fitness = [f / total_fitness for f in fitnesses]
        # Generate probability intervals for each individual
        probs = [sum(rel_fitness[:i + 1]) for i in range(len(rel_fitness))]
        # Draw new population
        new_population = []
        for n in xrange(population_to_keep):
            r = random.uniform(0.0, 1.0)
            for (i, individual) in enumerate(population.individuals):
                if r <= probs[i]:
                    new_population.append(individual)
                    break
        new_population += [best_solution] * elite_copy
        population.individuals = new_population
        return False


class Mutation(IOperator):

    def execute(self, environment, population, generation):
        for individual in population.individuals:
            individual.mutate()
        return False


class Crossover(IOperator):

    def execute(self, environment, population, generation):
        new_individuals = []
        needed = population.size - len(population.individuals)
        while len(new_individuals) < needed:
            a = random.choice(population.individuals)
            b = random.choice(population.individuals)

            if rand_probability() <= crossover_rate:
                new_individuals += a.crossover(b)
            else:
                new_individuals += [a, b]
        population.individuals += new_individuals
        return False


class Stop(IOperator):
    def execute(self, environment, population, generation):
        if generation >= max_generation:
            return True
        if environment.goal(population):
            return True
        return False
