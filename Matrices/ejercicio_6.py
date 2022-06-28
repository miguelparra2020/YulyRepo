# 6. Leer una matriz 4x4 entera y calcular el promedio de los números mayores de cada fila.

try:
    matriz = [[int(input("Ingresar numero")) for i in range(4)]  for i in range(4)]
    mayor_1 = 0
    mayor_2 = 0
    mayor_3 = 0
    mayor_4 = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i][:])):
            if i==0:
                if matriz[i][j]>mayor_1:
                    mayor_1=matriz[i][j]
            elif i==1:
                if matriz[i][j]>mayor_2:
                    mayor_2=matriz[i][j]
            elif i==2:
                if matriz[i][j]>mayor_3:
                    mayor_3=matriz[i][j]
            else:
                if matriz[i][j]>mayor_4:
                    mayor_4=matriz[i][j]
    promedio = (mayor_1+mayor_2+mayor_3+mayor_4)/4
    print("El numero mayor de la fila 1 es: ",mayor_1)
    print("El numero mayor de la fila 2 es: ",mayor_2)
    print("El numero mayor de la fila 3 es: ",mayor_3)
    print("El numero mayor de la fila 4 es: ",mayor_4)
    print("El promedio de los numeros mayores de cada fila es: ", promedio)
except ValueError: print("Error")