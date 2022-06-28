# 29. Leer una matriz 4x6 entera y determinar si alguno de sus números está repetido al menos 3 veces.

try:
    matriz = [[int(input("Ingresar numero para matriz 1:  ")) for i in range(4)]  for i in range(6)]
    lista = []

    for i in range(len(matriz)):
        for j in range(len(matriz[i][:])):
            lista.append(matriz[i][j])

    repetidos = []
    unicos = []
    cantidad = 0

    for i in lista:
        if i not in unicos:
            unicos.append(i)
        else:
            cantidad +=1
            if i not in repetidos:
                repetidos.append(i)
    print("Los numeros que estan repetidos son: ",repetidos)
    print(cantidad+1, "veces")

except ValueError: print("Error")