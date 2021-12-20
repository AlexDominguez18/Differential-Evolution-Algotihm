import copy

import numpy as np


class Individuo:
    def __init__(self, solucion):
        self._solucion = solucion
        self._fitness = 0

class DE:
    def __init__(self, cantidad_individuos, dimensiones, funcion, factor_mutacion, probabilidad_cruza, generaciones):
        self._cantidad_individuos = cantidad_individuos
        self._dimensiones = dimensiones
        self._funcion = funcion
        self._factor_mutacion = factor_mutacion
        self._probabilidad_cruza = probabilidad_cruza
        self._generaciones = generaciones
        self._individuos = []
        self._rango = self._funcion.MAX_VALUE - self._funcion.MIN_VALUE
        self._mejor = np.inf
        self._vector_mutante = []
        self._vector_prueba = []
        self._values = []

    def crearIndividuos(self):
        for i in range(self._cantidad_individuos):
            solucion = np.random.random(size = self._dimensiones) * self._rango + self._funcion.MIN_VALUE
            individuo = Individuo(solucion)
            self._individuos.append(individuo)

    def mejorIndividuo(self):
        for i in self._individuos:
            fitness = self._funcion.fitness(i._solucion)
            if fitness < self._mejor:
                self._mejor = fitness

    def run(self):
        self.crearIndividuos()
        generacion = 0
        while (generacion <= self._generaciones):    
            for i in range(len(self._individuos)):
                indices = [idx for idx in range(len(self._individuos)) if idx != i]
                copia_individuos = np.array(self._individuos)
                r1, r2, r3 = copia_individuos[(np.random.choice(indices, 3, replace=False))]
                self._vector_mutante.append(np.array(r1._solucion + self._factor_mutacion * (r2._solucion - r3._solucion)))
                Jr = np.random.randint(1,self._dimensiones + 1)
                for j in range(1, self._dimensiones + 1):
                    rcj = np.random.random(size = None)
                    if (rcj < self._probabilidad_cruza or j == Jr):
                        self._vector_prueba.append(self._vector_mutante[i])
                    else:
                        self._vector_prueba.append(self._individuos[i]._solucion)
            
            for i in range(len(self._individuos)):
                fitness_prueba = self._funcion.fitness(self._vector_prueba[i])
                fitness_individuo = self._funcion.fitness(self._individuos[i]._solucion)
                if (fitness_prueba < fitness_individuo):
                    #print(f"Prueba = {fitness_prueba}, Individuo = {fitness_individuo}")
                    self._individuos[i]._solucion = self._vector_prueba[i]

            if generacion % 100 == 0:
                self.mejorIndividuo()
                print('Generación ', generacion, ':', self._mejor)
                self._values.append(self._mejor)
            
            self._vector_mutante.clear()
            self._vector_prueba.clear()
            generacion += 1

    def getValues(self):
        return self._values
