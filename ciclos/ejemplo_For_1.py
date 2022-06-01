try:
    columna_1 = int(input("Por favor ingrese hasta que numero del 0 al 9 desea tener la primer columna"))
    columna_2 = int(input("Por favor ingrese hasta que numero del 0 al 9 desea tener la segunda columna"))
    for i in range(0,columna_1+1):
        for j in range(0,columna_2+1):
            print(i,j)
except ValueError:
    print("Error")