# 14. Leer una matriz 5x5 entera y determinar cuántos números almacenados en ella tienen más de 3 dígitos.

try:
    matriz = [[int(input("Ingresar numero")) for i in range(5)]  for i in range(5)]
    print(matriz)
    finalistas = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i][:])):
            if matriz[i][j] >= 100 or matriz[i][j] <= -100:
                finalistas.append(matriz[i][j])
    cantidad = len(finalistas)
    
    print("De los numeros ingresados hay: ",cantidad, "Números de 3 o más digitos")
except ValueError: print("Error")