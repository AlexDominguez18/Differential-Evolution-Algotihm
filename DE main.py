import quartic
import sphere 
import rastrigin 
import rosenbrock
import DE

import argparse
import numpy as np 
import matplotlib.pyplot as plt

MAX_EJECUCIONES = 5

def ejecutarFuncionDE(funcion, dimension):
    valoresY = []
    
    factor_mutacion = 0.8
    probabilidad_cruza = 0.7

    for i in range(MAX_EJECUCIONES):
        print(f"Ejecucion No. {i+1}")
        de = DE.DE(64, dimension, funcion, factor_mutacion, probabilidad_cruza, 2000)
        de.run()
        valoresY.append(de.getValues())
    
    for i in range(MAX_EJECUCIONES):
        for j in range(len(valoresY[i])):
            k=1
            while k < MAX_EJECUCIONES:
                valoresY[0][j] += valoresY[k][j]
                k = k + 1  
            valoresY[0][j] = valoresY[0][j]/5
    
    return valoresY[0]

def main():
 
    #Obteniendo informacion de los parametros
    parser = argparse.ArgumentParser()
    parser.add_argument('funcion')
    arg = parser.parse_args()

    if arg.funcion == "sphere":
        funcion = sphere.Sphere()
    elif arg.funcion == "rosenbrock":
        funcion = rosenbrock.Rosenbrock()
    elif arg.funcion == "rastrigin":
        funcion = rastrigin.Rastrigin()
    elif arg.funcion == "quartic":
        funcion = quartic.Quartic()
    else:
        print("Funcion no especificada.")
        exit

    #Valores del eje X
    x = [0,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000]
    
    print(f"{arg.funcion} in 2D:")
    y2d = ejecutarFuncionDE(funcion,2) 
    plt.plot(x, y2d, "r")
    nombreImagen = f'{arg.funcion}-2D'
    plt.title(nombreImagen)
    plt.savefig(nombreImagen + '.png')
    plt.show()
    print(f"{arg.funcion} in 4D:")
    y4d = ejecutarFuncionDE(funcion,4)
    plt.plot(x, y4d, "g")
    nombreImagen = f'{arg.funcion}-4D'
    plt.title(nombreImagen)
    plt.savefig(nombreImagen + '.png')
    plt.show()
    print(f"{arg.funcion} in 8D:")
    y8d = ejecutarFuncionDE(funcion,8)
    plt.plot(x, y8d, "b")
    nombreImagen = f'{arg.funcion}-8D'
    plt.title(nombreImagen)
    plt.savefig(nombreImagen + '.png')
    plt.show()
    
    #Imprimiendo grafica comparativa
    plt.plot(x, y2d, "r", label="2 Dimensiones")
    plt.plot(x, y4d, "g", label="4 Dimensiones")
    plt.plot(x, y8d, "b", label="8 Dimensiones")
    plt.legend()
    nombreImagen = f'{arg.funcion}-ALL'
    plt.title(nombreImagen)
    plt.savefig(nombreImagen + '.png')
    plt.show()

if __name__ == '__main__':
    main()
