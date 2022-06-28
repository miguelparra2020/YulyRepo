# 21. Leer dos matrices 4x5 enteras y determinar cuántos datos tienen en común.

try:
    matriz_1 = [[int(input("Ingresar numero para matriz 1:  ")) for i in range(2)]  for i in range(2)]
    matriz_2 = [[int(input("Ingresar numero para matriz 2:  ")) for i in range(2)]  for i in range(2)]
    repetidos = []
    cont1 = 0
    cont2 = 0

    for k in range(len(matriz_1)):
        for l in range(len(matriz_1[k][:])):
            cont1 = 0
            for g in range(len(matriz_2)):
                for s in range(len(matriz_2[g])):
                    if matriz_1[k][l] == matriz_2[g][s]:
                        cont1 += 1
                        
        if cont1 != 0:
            cont2 = 0
            for m in range(len(repetidos)):
                if matriz_1[k][l] == repetidos[m]:
                    cont2+=1
                            
            if cont2 == 0:
                repetidos.append(matriz_1[k][l])
    
        if len(repetidos) != 0:
            print("Los elementos en comun de las dos matrices son ",repetidos)
        
        else:
            print("Las dos matrices no tienen elementos en comun.")

except ValueError: print("Error")