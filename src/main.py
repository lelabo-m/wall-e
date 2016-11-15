from genetic_algorithm.algo import GeneticAlgorithm
from genetic_algorithm.env import Environment
from genetic_algorithm.genomes import GeneLibrary
from genetic_algorithm.individuals import Population
from genetic_algorithm.parameters import *
from src.simulation.client import RobotClient
from src.simulation.robot import Robot
import random
import time


def individual_to_sequence(individual):
    return [(move.x(), move.y(), move.z()) for move in individual.moves]

if __name__ == "__main__":
    print 'Start'
    random.seed()
    start = time.time()

    client = RobotClient()
    client.connect()
    if not client.is_connected():
        print "Connection failed!"
        exit(1)

    robot = Robot(client)
    if not robot.load():
        print "Robot initialization failed!"
        exit(1)


    GeneLibrary.init()
    algo = GeneticAlgorithm(Population(population_size), Environment(robot))
    algo.start(verbose=True)
    best_individual = algo.result()
    print best_individual
    print individual_to_sequence(best_individual)

    client.disconnect()
    end = time.time()
    print "Time elapsed: {}".format(end - start)
    print 'End'
