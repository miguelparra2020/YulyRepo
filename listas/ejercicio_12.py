# 12. Leer 10 números enteros, almacenarlos en una lista y determinar a cuánto es igual el
# promedio entero de los datos de la lista.
try:
    cantidad = int(input("Por favor ingresar la cantidad de numeros enteros"))
    lista = [int(input("ingresar numero:  ")) for i in range(cantidad) ]
    promedio = 0
    for i in range(cantidad):
        promedio += lista[i]
    promedio_final = int(promedio/cantidad)
    print("\nEl promedio de los numeros ingresados es: ",int(promedio_final))
except ValueError: print("Error")
