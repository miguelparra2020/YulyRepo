# 10. Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales.
try:
    numero = int(input("Por favor ingrese un numero entero de dos digitos para su validación"))

    if ( numero>=10 and numero<=99):
        num_1 = numero//10
        num_2 = numero%10
        if (num_1 == num_2):
            print("Los dos digitos del numero ingresado son Iguales")
        else:
            print("Los dos digitos NO son iguales")
    elif (numero>=(-99) and numero<=(-10)):
        num_positivo = numero*(-1)
        num_1 = num_positivo//10
        num_2 = num_positivo%10
        if (num_1 == num_2):
            print("Los dos digitos del numero ingresado son Iguales")
        else:
            print("Los dos digitos NO son iguales")
    else:
        print("No entra")
except ValueError:
    print("El dato ingresado es Erroneo")

