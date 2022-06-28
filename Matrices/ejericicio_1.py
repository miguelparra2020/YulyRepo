# 1. Leer una matriz 4x4 entera y determinar en qué fila y en qué columna se encuentra el
# número mayor. 

try:
    matriz = [[int(input("Ingresar numero")) for i in range(4)]  for i in range(4)]
    mayor = 0
    for i in range(len(matriz[0][:])):
        for j in range(len(matriz[:])):
            if matriz[i][j]>mayor:
                mayor=matriz[i][j]
    print("El número mayor de la matriz es: ", mayor)
except ValueError: print("Error")