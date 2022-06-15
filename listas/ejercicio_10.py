# 10. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se
# encuentran los números con más de 3 dígitos.
try:
    lista = [int(input("ingresar numero:  ")) for i in range(10) ]
    mayores = [i+1 for i in range(10) if lista[i]>999]
    print("Las posiciones de los numeros de más de 3 digitos es: ",mayores)
except ValueError: print("Error")