import numpy as np

class Rastrigin:
    
    MIN_VALUE = -5.12
    MAX_VALUE = 5.12
    
    def __init__(self):
        pass
    
    def fitness(self, vector):
        z = 0
        for dimension in vector:
            z += (10 * Rastrigin.MAX_VALUE) + dimension ** 2 - (10 * np.cos(2 * np.pi * dimension))
        return z
