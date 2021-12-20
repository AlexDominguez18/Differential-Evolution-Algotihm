class Quartic:

    MIN_VALUE = -1.28
    MAX_VALUE = 1.28
    
    def __init__(self):
        pass
    
    def fitness(self, vector):
        z = 0
        for dimension in vector:
            z += (Quartic.MIN_VALUE * dimension) ** 4
        return z
