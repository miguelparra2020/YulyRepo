# 7. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se encuentra el número mayor.
try:
    cantidad = int(input("Por favor ingrese la cantidad de numeros a solicitar: "))
    lista = [int(input("Ingrese un numero: ")) for i in range(cantidad)]
    print("El numero mayor de la lista es: ",max(lista), " y se encuentra en la posición: ",lista.index(max(lista))+1)
except ValueError: print("Error")