# 23. Leer dos matrices 4x5 enteras y determinar si el número mayor 
# de una de las matrices es igual al número mayor de la otra matriz.

try:
    matriz_1 = [[int(input("Ingresar numero para matriz 1:  ")) for i in range(4)]  for i in range(5)]
    matriz_2 = [[int(input("Ingresar numero para matriz 2:  ")) for i in range(4)]  for i in range(5)]
    lista_1 = []
    lista_2 = []
    for i in range(len(matriz_1)):
        for j in range(len(matriz_1[i][:])):
                lista_1.append(matriz_1[i][j])
    for k in range(len(matriz_2)):
        for l in range(len(matriz_2[k][:])):
                lista_2.append(matriz_2[k][l])
    
    if max(lista_1) == max(lista_2):
        print("El numero mayor de la matriz 1 es:", max(lista_1)," y esigual al numero mayor de la matriz 2", max(lista_2) )
    else:
        print("Los numeros mayores de las matrices no son iguales")

except ValueError: print("Error")