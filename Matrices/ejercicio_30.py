# 30. Leer una matriz 4x6 entera y determinar cuántas veces está en ella el número menor.

try:
    matriz = [[int(input("Ingresar numero para matriz 1:  ")) for i in range(4)]  for i in range(6)]
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i][:])):
            lista.append(matriz[i][j])
    menor = min(lista)
    cantidad = lista.count(menor)
    print("El numero menor está:",cantidad, "Veces")

except ValueError: print("Error")