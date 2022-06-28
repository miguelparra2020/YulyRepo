# 22. Leer dos matrices 4x5 enteras y determinar si el número mayor almacenado en la primera está en la segunda.

try:
    matriz_1 = [[int(input("Ingresar numero para matriz 1:  ")) for i in range(4)]  for i in range(5)]
    matriz_2 = [[int(input("Ingresar numero para matriz 2:  ")) for i in range(4)]  for i in range(5)]
    mayor = max(max(matriz_1))
    print(mayor)
    print(matriz_2)
    buscar = []
    for i in range(len(matriz_2)):
        for j in range(len(matriz_2[i][:])):
            if matriz_2[i][j] == mayor:
                buscar.append("El numero mayor de la lista 1 es:",mayor,"y se encuentra almacenado en la lista 2")
    print(buscar[0])
    
except ValueError: print("Error")