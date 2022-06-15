# 11. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números
# tienen, de los almacenados allí, menos de 3 dígitos.
try:
    cantidad = int(input("Por favor ingresar la cantidad de numeros enteros"))
    lista = [int(input("ingresar numero:  ")) for i in range(cantidad) ]
    contador = 0
    for i in range(cantidad):
        if lista[i] >= (-999) and lista[i] <= 999:
            contador += 1
    print("En la lista hay: ", contador, "Numeros que tienen menos de 3 digitos")
except ValueError: print("Error")