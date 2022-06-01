''''Solicitar al usuario un numero enteros de 3 cifras, para sacar el area de un triangulo e imprimir su resultado'''

num_1 = int(input("Digite el primer número de 3 cifras"))

num_2 = num_1//100
num_3 = num_1%100
num_4 = num_3//10
num_5 = num_3%10
print("numero 1 es :" + str(num_2),"numero 2 es :" + str(num_4),"numero 3 es :" + str(num_5))