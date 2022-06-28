# 2. Leer una matriz 4x4 entera y determinar cuántas veces se repita en ella el número mayor.

try:
    matriz = [[int(input("Ingresar numero")) for i in range(4)]  for i in range(4)]
    mayor = 0
    contador = 0
    for i in range(len(matriz[0][:])):
        for j in range(len(matriz[:])):
            if matriz[i][j]>mayor:
                mayor=matriz[i][j]
    
    for i in range(0,len(matriz)):
        contador += matriz[i][:].count(mayor)    
    
    print("El número mayor de la matriz es: ", mayor, "y en la lista se encuentra repetido: ",contador,"veces")
except ValueError: print("Error")