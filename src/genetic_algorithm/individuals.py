from interfaces import IIndividual, IPopulation
from parameters import *
from genomes import *
from operator import attrgetter
from utils import rand_probability
import copy


class Movement:

    def __init__(self, empty=False):
        self.genes = []
        if not empty:
            for i in range(3):
                self.genes.append(Genes.random())

    def __str__(self):
        return "Move(x={},y={},z={})".format(self.x(), self.y(), self.z())

    def __repr__(self):
        return str(self)

    def x(self):
        return self.genes[0].value

    def y(self):
        return self.genes[1].value

    def z(self):
        return self.genes[2].value

    def mutate(self):
        for gene in self.genes:
            if rand_probability() <= mutation_rate:
                gene.mutate()

    def crossover(self, other):
        move_a = Movement(empty=True)
        move_b = Movement(empty=True)
        for index in range(3):
            a = self.genes[index]
            b = other.genes[index]
            gene_a, gene_b = a.crossover(b)
            move_a.genes.append(gene_a)
            move_b.genes.append(gene_b)
        return move_a, move_b


class Individual(IIndividual):

    def __init__(self, empty=False):
        IIndividual.__init__(self)
        if not empty:
            self.moves = [Movement() for x in range(nb_move)]
        self.fitness = 0.0

    def __str__(self):
        return "Individual(fitness={}, moves={})".format(self.fitness, ",".join([str(move) for move in self.moves]))

    def __repr__(self):
        return str(self)

    def copy(self):
        return copy.deepcopy(self)

    def mutate(self):
        for move in self.moves:
            move.mutate()

    def crossover(self, other):
        indiv_a = Individual(empty=True)
        indiv_b = Individual(empty=True)
        size = max(len(self.moves), len(other.moves))
        for index in range(size):
            a = self.move_at(index)
            b = other.move_at(index)
            move_a, move_b = a.crossover(b)
            # Todo: preserve size of parent
            indiv_a.moves.append(move_a)
            indiv_b.moves.append(move_b)
        return [indiv_a, indiv_b]

    def move_at(self, index):
        return self.moves[index % len(self.moves)]


class Population(IPopulation):

    def __init__(self, pop):
        IPopulation.__init__(self)
        self.size = pop

    def init(self):
        self.individuals = [Individual() for x in range(self.size)]

    def fitnesses(self):
        return [individual.fitness for individual in self.individuals]

    def best(self):
        return max(self.individuals, key=attrgetter('fitness')).copy()
