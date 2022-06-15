# 1. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de la lista está el mayor número leído.
try:
    cantidad = int(input("Por favor ingrese la candidad de numeros a solicitar"))
    lista = [int(input("ingrese numero:  ")) for i in range(cantidad)]
    mayor = [max(lista[i] for i in range(cantidad))]
    print("De los numeros ingresados, el numero: ",mayor[0], "Es el mayor y está en la posición de la lista: ",lista.index(mayor[0])+1)   
except ValueError:print("Error")