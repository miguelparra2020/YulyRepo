# 19. Leer dos matrices 4x5 entera y determinar si sus contenidos son exactamente iguales.
try:
    matriz_1 = [[int(input("Ingresar numero para matriz 1:  ")) for i in range(4)]  for i in range(5)]
    matriz_2 = [[int(input("Ingresar numero para matriz 2:  ")) for i in range(4)]  for i in range(5)]
    print(matriz_1)
    print(matriz_2)
    if matriz_1 == matriz_2:
        print("Las matrices son exactamente igual")
    else:
        print("No son iguales")
    
except ValueError: print("Error")