from genetic_algorithm.individuals import Population
from genetic_algorithm.env import Environment
from genetic_algorithm.algo import GeneticAlgorithm
from genetic_algorithm.genomes import GeneLibrary
from genetic_algorithm.parameters import *

GeneLibrary.init()
algo = GeneticAlgorithm(Population(population_size), Environment())
algo.start()
best_individual = algo.result()
print best_individual