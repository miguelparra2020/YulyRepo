# 20. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición está el menor número primo.

try:
    cantidad = int(input("Por favor ingresar la cantidad de numeros enteros que va a ingresar     "))
    lista = [int(input("Ingresar numero:  ")) for i in range(cantidad)]
    primo = []
    for i in range(cantidad):
        contador = 0
        for j in range(2,(lista[i]//2)+1):
            if (lista[i])%j ==0:
                contador += 1
        if contador == 0:
            primo.append(lista[i])
    menor_primo = min(primo)
    print("El numero primo menor que se encuentra en la lista es: ",menor_primo,"y está en la posición",lista.index(menor_primo)+1)
except ValueError: print("Error")