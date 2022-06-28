# GC-F -005 V. 05
# 13. Leer una matriz 5x3 entera y determinar en qué columna está el mayor número que comienza con el dígito 4.

try:
    matriz = [[int(input("Ingresar numero")) for i in range(5)]  for i in range(3)]
    print(matriz)
    finalistas = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i][:])):
            if int(str(matriz[i][j])[0]) == 4:
                print("El numero: ",matriz[i][j],"Empieza en 4" )
                finalistas.append([matriz[i][j],j+1])
    mayor = max(finalistas)
    print("El numero que mayor que empieza en 4 es: ",mayor[0])
    print("Este numero está en la columna: ",mayor[1])
except ValueError: print("Error")