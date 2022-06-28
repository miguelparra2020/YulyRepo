# 3. Leer una matriz 3x4 entera y determinar en qué posiciones exactas se encuentran los números pares.

try:
    matriz = [[int(input("Ingresar numero")) for i in range(3)]  for i in range(4)]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i][:])):
            if matriz[i][j]%2==0:
                print("Numero par en está en la columna: ",i,"Fila",j)
    
except ValueError: print("Error")