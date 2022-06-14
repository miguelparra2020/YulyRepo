#lista 10 elementos, Enteros positivos 
try:
    num = int(input("Cantidad de numeros a ingresar     "))
    lista_1 = [int(input("Ingresar numero  ")) for i in range(num)] 
    lista_2 = [lista_1[i]**3 for i in range(num)]
    print(lista_2)
except ValueError:
    print("Error")

