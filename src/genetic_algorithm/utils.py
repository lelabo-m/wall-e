import random
import math


def rand_probability():
    return float(random.randint(0, 100)) / 100.0


def euclidean_distance(start, end):
    return math.sqrt((start[0] - end[0])**2 + (start[1] - end[1])**2)
