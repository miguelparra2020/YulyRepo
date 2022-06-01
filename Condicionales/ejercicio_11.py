# 11. Leer dos números enteros y determinar cuál es el mayor.
try:
    numero = int(input("Por favor ingrese un numero entero de dos digitos para su validación"))

    if (numero>=10 and numero<=99):
        num_1 = numero//10
        num_2 = numero%10
        if (num_1 > num_2):
            print("Del número ingresado: "+str(numero)+", el primer digito: ", num_1, " es mayor que el segundo digito: ", num_2)
        elif (num_2 > num_1):
            print("Del número ingresado: "+str(numero)+", el segundo digito: ", num_2, " es mayor que el primer digito: ", num_1)
    elif ((numero>=(-99) and numero<=(-10) )):
        num_positivo = numero*(-1)
        num_1 = num_positivo//10
        num_2 = num_positivo%10
        if (num_1 > num_2):
            print("Del número ingresado: "+str(numero)+", el primer digito: ", num_1, " es mayor que el segundo digito: ", num_2)
        elif (num_2 > num_1):
            print("Del número ingresado: "+str(numero)+", el segundo digito: ", num_2, " es mayor que el primer digito: ", num_1)
    else:
        print("No entra")
except ValueError:
    print("El dato ingresado es Erroneo")