# 13. Leer 10 números enteros, almacenarlos en una lista y determinar si el promedio entero
# de estos datos está almacenado en la lista.
try:
    cantidad = int(input("Por favor ingresar la cantidad de numeros enteros"))
    lista = [int(input("ingresar numero:  ")) for i in range(cantidad) ]
    promedio = 0
    for i in range(cantidad):
        promedio += lista[i]
    promedio_final = int(promedio/cantidad)
    print("\nEl promedio de los numeros ingresados es: ",int(promedio_final))
    buscar = int(lista.index(int(promedio_final)))+1
    if promedio_final == buscar:
        print("El promedio de los numeros ingresados SI está en la lista")
    else:
        print("El promedio no está en la lista")

except ValueError: print("Error")