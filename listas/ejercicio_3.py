# 3. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de la lista está
# el mayor número primo leído.

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
    mayor_primo = max(primo)
    print("El numero primo mayor que se encuentra en la lista es: ",mayor_primo,"y está en la posición",lista.index(mayor_primo)+1)
except ValueError: print("Error")