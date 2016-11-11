import random

nb_population = 300
nb_population_to_keep = 200
nb_move = 3
max_generation = 1000
mutation_rate = 0.01


class IIndividual(object):
    def __init__(self):
        self.genes = None
        self.score = None

    def mutate(self, gene):
        pass


class IPopulation(object):
    def __init__(self):
        self.individus = []


class IEnvironment(object):
    def fitness(self, individu):
        pass


class IOperator(object):
    def execute(self, environment, population, generation_number):
        pass


def all_fitnesses(individus):
    fitnesses = []
    for ind in individus:
        fitnesses.append(ind.score)
    return fitnesses


class Selection(IOperator):
    def execute(self, environment, population, generation_number):
        fitnesses = all_fitnesses(population.individus)
        total_fitness = sum(fitnesses)
        rel_fitness = [f / total_fitness for f in fitnesses]
        # Generate probability intervals for each individual
        probs = [sum(rel_fitness[:i + 1]) for i in range(len(rel_fitness))]
        # Draw new population
        new_population = []
        for n in xrange(nb_population_to_keep):
            r = random.random()
            for (i, individual) in enumerate(population.individus):
                if r <= probs[i]:
                    new_population.append(individual)
                    break
        children = generate_individuals(nb_population - nb_population_to_keep)
        for child in children:
            environment.fitness(child)
        new_population.extend(children)
        population.individus = new_population


class Mutation(IOperator):
    def execute(self, environment, population, generation_number):
        # fixme: maybe to review
        for individu in population.individus:
            if (random.randint(0, 100)) / 100 <= mutation_rate:
                individu.genes.x = individu.mutate(individu.genes.x)
                environment.fitness(individu)

            if (random.randint(0, 100)) / 100 <= mutation_rate:
                individu.genes.y = individu.mutate(individu.genes.y)
                environment.fitness(individu)

            if (random.randint(0, 100)) / 100 <= mutation_rate:
                individu.genes.z = individu.mutate(individu.genes.z)
                environment.fitness(individu)


class Crossover(IOperator):
    def execute(self, environment, population, generation_number):
        # TODO: implemente Crossover
        # TODO: recalc fitness
        pass


class Stop(IOperator):
    def execute(self, environment, population, generation_number):
        if generation_number >= max_generation:
            algo.stop()


def generate_individuals(pop):
    i = 0
    inds = []
    while i < pop:
        ind = Individual()
        x = random.randint(0, 360)
        y = random.randint(0, 360)
        z = random.randint(0, 360)
        ind.genes = Genomes(nb_move, x, y, z)
        inds.append(ind)
        i += 1
    return inds


class Population(IPopulation):
    def __init__(self, pop):
        IPopulation.__init__(self)
        self.individus = generate_individuals(pop)
        self.populationNumber = pop


class Environment(IEnvironment):
    def __init__(self):
        self.goal = None
        # TODO: implemente goal

    def fitness(self, individu):
        individu.score = 1
        # TODO: implemente Fitness
        pass


class Genomes(object):
    def __init__(self, n, x, y, z):
        self.n = n
        self.x = x
        self.y = y
        self.z = z


class Individual(IIndividual):
    def __init__(self):
        IIndividual.__init__(self)
        self.genes = None
        self.score = None

    def mutate(self, gene):
        # TODO: mutation
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
        self.generation_number = 0
        self._stop = False

    def init_population(self):
        for individu in self.population.individus:
            self.environment.fitness(individu)

    def execute_operators(self):
        for op in self.operators:
            op.execute(self.environment, self.population, self.generation_number)

    def start(self):
        self.init_population()
        print "generation_number, max, min, avg"
        while self._stop is False:
            self.execute_operators()
            fitnesses = all_fitnesses(self.population.individus)
            print "{}, {}, {}, {}".format(self.generation_number, max(fitnesses), min(fitnesses),
                  reduce(lambda x, y: x + y, fitnesses) / len(fitnesses))
            self.generation_number += 1

    def stop(self):
        self._stop = True


algo = AlgoGen(Population(nb_population), Environment())
algo.start()
