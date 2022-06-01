# 10.Ejemplo
try:
    inicio = int(input("Por favor ingrese el inico"))
    fin = int(input("Por favor ingrese el fin"))
    incre_decre = int(input("Por favor ingrese el numero de incremento positivo o negativo si es decremento"))

    for i in range(inicio,fin+1,incre_decre):
        print(i)
except ValueError:
    print("El dato ingresado es Erroneo")