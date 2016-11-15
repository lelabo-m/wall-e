import random
from utils import rand_probability
from parameters import mixing_ratio

class GeneLibrary:

    __ints = {}
    __bits = {}

    def __init__(self):
        self.__generate()

    @classmethod
    def init(cls):
        cls.__generate()

    @classmethod
    def __generate(cls):
        for i in range(0, 512):
            bits = format(i, '09b')
            cls.__ints[i] = bits
            cls.__bits[bits] = i

    @classmethod
    def int_to_bits(cls, value):
        return cls.__ints[value]

    @classmethod
    def bits_to_int(cls, value):
        return cls.__bits[value]

    @classmethod
    def normalize(cls, value):
        return value % 361


class Genes:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Genes(value={})".format(self.value)

    def __repr__(self):
        return str(self)

    @classmethod
    def random(cls):
        return Genes(random.randint(0, 360))

    def mutate(self):
        print "MUTATE"
        bits = [int(bit) for bit in GeneLibrary.int_to_bits(self.value)]
        index = random.randint(0, 8)
        bits[index] = int(not bits[index])
        self.value = GeneLibrary.normalize(GeneLibrary.bits_to_int("".join([str(bit) for bit in bits])))

    # uniform crossover
    def crossover(self, other):
        a_bits = [int(bit) for bit in GeneLibrary.int_to_bits(self.value)]
        b_bits = [int(bit) for bit in GeneLibrary.int_to_bits(other.value)]
        for index in range(9):
            if rand_probability() <= mixing_ratio:
                tmp = a_bits[index]
                a_bits[index] = b_bits[index]
                b_bits[index] = tmp
        a_value = GeneLibrary.normalize(GeneLibrary.bits_to_int("".join([str(bit) for bit in a_bits])))
        b_value = GeneLibrary.normalize(GeneLibrary.bits_to_int("".join([str(bit) for bit in b_bits])))
        return Genes(a_value), Genes(b_value)
