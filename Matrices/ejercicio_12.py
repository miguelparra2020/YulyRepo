# 12. Leer una matriz 5x5 entera y determinar en qué fila está el mayor número terminado en 6.

try:
    matriz = [[int(input("Ingresar numero")) for i in range(5)]  for i in range(5)]
    finalistas = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i][:])):
            if matriz[i][j]%10 == 6:
                print("El numero ",matriz[i][j],"termina en 6")
                finalistas.append([matriz[i][j],i+1])
    numero = max(finalistas)

    print("El numero mayor terminado en 6 es el: ",numero[0])
    print("El numero se encuentra en la fila. ",numero[1])


except ValueError: print("Error")