# 17. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números negativos hay.
try:
    cantidad = int(input("Por favor ingresar la cantidad de numeros enteros que va a ingresar     "))
    lista = [int(input("Ingresar numero:  ")) for i in range(cantidad)]
    negativos = [lista[i] for i in range(cantidad) if lista[i]<0]
    print("De los numeros ingresados, hay: ", len(negativos),"numeros negativos")
except ValueError: print("Error")