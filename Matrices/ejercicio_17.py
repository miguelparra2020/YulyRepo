# 17. Leer una matriz 5x4 entera y determinar cuántos múltiplos de 5 hay almacenados en ella.

try:
    matriz = [[int(input("Ingresar numero")) for i in range(5)]  for i in range(4)]
    print(matriz)
    finalistas = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i][:])):
            if matriz[i][j]%5==0:
                finalistas.append(matriz[i][j])
    print(finalistas)
    cantidad = len(finalistas)
    print("De los numeros ingresados hay: ",cantidad, "Números multiplos de 5")
except ValueError: print("Error")