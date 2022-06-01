try:
    num = int(input("Por favor ingrese el numero"))
    cont = 0

    while num != 0:
        cont += 1
        num//=10
    print(" El numero ingresado tiene ", cont, "Digitos")
except ValueError:
    print("Error")