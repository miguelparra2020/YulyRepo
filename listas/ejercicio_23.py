# 23. Leer 10 números enteros, almacenarlos en una lista y determinar si existe al menos un número repetido.

try:
    cantidad = int(input("Por favor ingrese la candidad de numeros a solicitar"))
    lista = [int(input("ingresar numero:  ")) for i in range(cantidad) ]
    repeticion = 0
    numero = 0
    for i in lista:
        if lista.count(i)>1:
            repeticion = lista.count(i)
            numero = i
    print("El numero: ",numero,"Está repetido:", repeticion, "veces")

except ValueError: print("Error")