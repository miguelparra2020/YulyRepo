from operator import index


try:
    lista_1 = [max(int(input("ingrese numero:  ")) for i in range(10))]
    print(lista_1)
except ValueError:print("Error")