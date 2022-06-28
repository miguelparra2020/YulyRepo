# 8. Leer una matriz 4x4 entera y determinar cuántos enteros terminados en 0 hay almacenados en ella.

try:
    matriz = [[int(input("Ingresar numero")) for i in range(4)]  for i in range(4)]
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i][:])):
            if matriz[i][j]%10 == 0:
                print("El numero ",matriz[i][j],"Termina en 0")
                contador += 1
    print("Hay: ", contador," Numeros que terminan en 0")
except ValueError: print("Error")