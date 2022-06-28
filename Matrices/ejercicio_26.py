# 26. Leer dos matrices 4x5 enteras y determinar si la cantidad de números pares almacenados en una matriz es igual 
# a la cantidad de números pares almacenados en la otra matriz.

try:
    matriz_1 = [[int(input("Ingresar numero para matriz 1:  ")) for i in range(4)]  for i in range(5)]
    matriz_2 = [[int(input("Ingresar numero para matriz 2:  ")) for i in range(4)]  for i in range(5)]
    pares_1 = []
    pares_2 = []
    for i in range(len(matriz_1)):
        for j in range(len(matriz_1[i][:])):
            if matriz_1[i][j]%2==0:
                pares_1.append(matriz_1[i][j])
    for k in range(len(matriz_2)):
        for l in range(len(matriz_2[k][:])):
            if matriz_2[k][l]%2==0:
                pares_2.append(matriz_2[k][l])

    if len(pares_1)==len(pares_2):
        print("La primer matriz tiene:",len(pares_1),"Numeros pares y la segunda matriz tiene la misma cantidad")
    else:
        print("Las dos matrices No tienen la misma cantidad de numeros pares")

except ValueError: print("Error")