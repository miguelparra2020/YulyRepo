# 16. Leer una matriz 5x4 entera y determinar cuántos números almacenados en ella tienen un solo dígito.

try:
    matriz = [[int(input("Ingresar numero")) for i in range(5)]  for i in range(5)]
    print(matriz)
    finalistas = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i][:])):
            if matriz[i][j] >= -9 and matriz[i][j] <= 9:
                finalistas.append(matriz[i][j])
    cantidad = len(finalistas)
    print("De los numeros ingresados hay: ",cantidad, "Números de un 1 digito")
except ValueError: print("Error")