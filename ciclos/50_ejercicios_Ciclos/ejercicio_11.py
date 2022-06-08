# 11.  Leer  un  número  entero  de  dos  dígitos  y  mostrar  
# en  pantalla  todos  los  enteros comprendidos entre undígito y otro

try:
    numero = int(input("Por favor ingrese un numero entero de dos digitos"))
    
    if (numero>=10 and numero<=99):
        num_1 = numero//10
        num_2 = numero%10
        for i in range(num_1, num_2+1):
            print(i)
        for i in range(num_2, num_1+1):
            print(i)
    elif (numero>=(-99) and numero<=(-10)):
        num_positivo = numero*(-1)
        num_1 = num_positivo//10
        num_2 = num_positivo%10
        for i in range(num_1, num_2+1):
            print(i*(-1))
        for i in range(num_2, num_1+1):
            print(i*(-1))
    else:
        print("El numero ingresado NO es de dos digitos")
except ValueError:
    print("Error")