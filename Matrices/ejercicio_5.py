# 5. Leer una matriz 4x3 entera,
#  calcular la suma de los elementos de cada fila y determinar cuál es la fila que tiene la mayor suma.

try:
    matriz = [[int(input("Ingresar numero")) for i in range(3)]  for i in range(4)]
    suma_1 = 0
    suma_2 = 0
    suma_3 = 0
    suma_4 = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i][:])):
            if i==0:
                suma_1 += matriz[i][j]
            elif i==1:
                suma_2 += matriz[i][j]
            elif i==2:
                suma_3 += matriz[i][j]
            else:
                suma_4 += matriz[i][j]
    print("La suma de la fila 1 es: ",suma_1)
    print("La suma de la fila 2 es: ",suma_2)
    print("La suma de la fila 3 es: ",suma_3)
    print("La suma de la fila 4 es: ",suma_4)

except ValueError: print("Error")