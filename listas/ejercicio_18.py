# 18. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones están los números positivos.
try:
    cantidad = int(input("Por favor ingresar la cantidad de numeros enteros que va a ingresar     "))
    lista = [int(input("Ingresar numero:  ")) for i in range(cantidad)]
    positivos = [lista[i] for i in range(cantidad) if lista[i]>=0]            
    posiciones = [i+1 for i in range(cantidad) if lista[i]>=0]
    print("De los numeros ingresados, estos: ", positivos,"son positivos y estan en las posiciones: ", posiciones )
except ValueError: print("Error")