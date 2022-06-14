try:
    num_ingresar = int(input("por favor ingresar un número para validar si el numero es de dos cifras y termina en cero"))

    if(num_ingresar>=10 and num_ingresar<=99) and (num_ingresar%10 == 0):
        print("Correcto!! Este número es de dos cifras y termina en cero")
    else:
        print("Incorrecto!! El numero no cumple")
except ValueError:
    print("El valor ingresado no es un numero entero")