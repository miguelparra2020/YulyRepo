# 18. Leer una matriz 5x5 entera y determinar en qué posición exacta se encuentra el mayor múltiplo de 8.
try:
    matriz = [[int(input("Ingresar numero")) for i in range(5)]  for i in range(4)]
    print(matriz)
    finalistas = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i][:])):
            if matriz[i][j]%8==0:
                finalistas.append([matriz[i][j],i,j])
    cantidad = max(finalistas)
    print("De los numeros ingresados el mayor multiplo de 8 es: ",cantidad[0],"Este se encuenta en la posición:","Fila:",cantidad[1]+1,"Columna:",cantidad[2]+1)
except ValueError: print("Error")