from interfaces import IEnvironment
from parameters import stopping_criterion, population_size
from src.simulation.simulation import Simulation
from utils import euclidean_distance
import math
import time

count = 0


class Environment(IEnvironment):
    def __init__(self, robot):
        self.robot = robot
        self.register = {}

    @classmethod
    def moves_to_str(cls, individual):
        chunks = []
        for move in individual.moves:
            chunks.append("{}-{}-{}".format(move.x(), move.y(), move.z()))
        return "+".join(chunks)

    @classmethod
    def goal(cls, population):
        global count
        print count
        count = 0

        candidate_solution = population.best()
        if candidate_solution.fitness >= stopping_criterion:
            return True
        return False

    def simulate(self, individual):
        self.robot.client.display_activation(False)
        simulation = Simulation(self.robot.client)
        simulation.start()
        self.robot.init_stream()
        time.sleep(0.1)
        start = self.robot.position

        for move in individual.moves:
            self.robot.pause(True)
            self.robot.wrist = math.radians(move.x())
            self.robot.elbow = math.radians(move.y())
            self.robot.shoulder = math.radians(move.z())
            self.robot.pause(False)
            self.robot.wait()

        end = self.robot.position
        simulation.stop()
        time.sleep(0.1)
        return euclidean_distance(start, end)

    def fitness(self, individual):
        global count
        print count
        count += 1

        move_key = self.moves_to_str(individual)
        if move_key not in self.register:
            self.register[move_key] = self.simulate(individual)
        else:
            print "EXIST"
        individual.fitness = self.register[move_key]

    def evaluate(self, population):
        [self.fitness(individual) for individual in population.individuals]
