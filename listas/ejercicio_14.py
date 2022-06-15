# 14. Leer 10 números enteros, almacenarlos en una lista y
#  determinar cuántas veces se repite el promedio entero de los datos dentro de la lista.

try:
    cantidad = int(input("Por favor ingresar la cantidad de numeros enteros que va a ingresar     "))
    lista = [int(input("Ingresar numero:  ")) for i in range(cantidad)]
    promedio = 0
    for i in range(cantidad):
        promedio += lista[i]
    promedio_final = int(promedio/cantidad)
    print("El promedio entero de la lista es: ", promedio_final, "y se repite: ", lista.count(promedio_final), "veces")
except ValueError: print("Error")