# 8. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se encuentran los números terminados en 4.
try:
    cantidad = int(input("Por favor ingrese la cantidad de numeros a solicitar: "))
    lista = [int(input("Ingrese un numero: ")) for i in range(cantidad)]
    terminan_4 = []
    posiciones = []
    for i in range(cantidad):
        if lista[i]%10==4:
            terminan_4.append(lista[i])
            posiciones.append(lista.index(lista[i])+1)
    print("De los numeros ingresados, los que terminan en 4 son: ", terminan_4, "y estos tienen las posiciones", posiciones)
except ValueError: print("Error")