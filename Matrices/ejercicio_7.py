# 7. Leer una matriz 4x4 entera y determinar en qué posiciones están los enteros terminados en 0.

try:
    matriz = [[int(input("Ingresar numero")) for i in range(4)]  for i in range(4)]
    for i in range(len(matriz)):
        for j in range(len(matriz[i][:])):
            if matriz[i][j]%10 == 0:
                print("Enumero ",matriz[i][j],"Termina en 0 y se encuentra en la posición: ","Columna:",i,"Fila:",j )
except ValueError: print("Error")