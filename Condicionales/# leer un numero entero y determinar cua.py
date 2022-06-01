# leer un numero entero y determinar cuantos digitos tiene 

try:

    numero = int(input("ingrese un numero: "))

    cont = 0

    while numero != 0:

        numero = numero // 10

        cont = cont + 1

    print ("su numero tiene una cantidad de",cont,"digitos")

except ValueError:

    print ("el numero ingresado es invalido, por favor verificar y volver a ejecutar")


