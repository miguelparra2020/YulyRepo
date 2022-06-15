# 9. Leer 10 números enteros, almacenarlos en una lista y determinar cuántas veces está repetido el mayor.

try:
    cantidad = int(input("Por favor ingrese la cantidad de numeros a solicitar: "))
    lista = [int(input("Ingrese un numero: ")) for i in range(cantidad)]
    print("El numero mayor de la lista es: ",max(lista), " y se repite: ",lista.count(max(lista)))
except ValueError: print("Error")