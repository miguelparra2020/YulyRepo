# 16. Leer 10 números enteros, almacenarlos en una lista y determinar cuáles son los datos almacenados múltiplos de 3.

try:
    cantidad = int(input("Por favor ingresar la cantidad de numeros enteros que va a ingresar     "))
    lista = [int(input("Ingresar numero:  ")) for i in range(cantidad)]
    multiplos_3 = [lista[i] for i in range(cantidad) if lista[i]%3==0]
    print("De los numeros ingresados, estos: ", multiplos_3,"Son multiplos de 3")
except ValueError: print("Error")