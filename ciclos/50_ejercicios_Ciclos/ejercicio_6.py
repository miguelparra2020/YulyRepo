# 6. Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos entre 1
# y cada uno de los dígitos.
try:
    numero_1 = int(input("Por favor ingresar un numero entero de tres digitos"))

    if (numero_1>=100 and numero_1<=999):
        num_1 = numero_1//100
        num_2 = (numero_1//10)%10
        num_3 = numero_1%10 
        print("Del numero ingresado tienen los siguientes digitos  ",num_1,num_2, num_3)
        for i in range(1, num_1+1):
            print("Del primer digito:     ", i)
        print("")
        for j in range(1, num_2+1):
            print("Del segundo digito:     ", j)
        print("")
        for k in range(1, num_3+1):
            print("Del tercer digito:     ", k)
    elif (numero_1>=-999 and numero_1<=-100):
        num_1_positivo = numero_1*(-1)
        num_1 = num_1_positivo//100
        num_2 = (num_1_positivo//10)%10
        num_3 = num_1_positivo%10 
        print("Del numero ingresado tienen los siguientes digitos  ",num_1*(-1),num_2*(-1), num_3*(-1))
        for i in range(num_1*(-1),0):
            print("Del primer digito:     ", i)
        print("")
        for j in range(num_2*(-1),0):
            print("Del segundo digito:     ", j)
        print("")
        for k in range(num_3*(-1), 0):
            print("Del tercer digito:     ", k)
    else:
        ("El numero ingresado no es de tres digitos")
except ValueError:
    print("Error")