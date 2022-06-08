# 12. Leer un número entero de 3 dígitos y determinar si tiene el dígito 1

try:
    numero = int(input("Por favor ingrese un numero entero de 3 digitos"))
    
    if (numero>=100 and numero<=999):
        num_1 = numero//100
        num_2 = (numero//10)%10
        num_3 = numero%10
        while (num_1==1 or num_2==1 or num_3==1):
            print("En el numero ingresado está el digito 1")
            break
        while (num_1==0 or num_2==0 or num_3==0 or
                num_1==1 or num_2==0 or num_3==0 or
                num_1==0 or num_2==0 or num_3==0 or
                num_1==0 or num_2==0 or num_3==0 or
                num_1==0 or num_2==0 or num_3==0 or
                num_1==0 or num_2==0 or num_3==0 or
                num_1==0 or num_2==0 or num_3==0 ):
            print("En el numero ingresado está el digito 1")
            break
    elif (numero>=(-999) and numero<=(-100)):
        num_positivo = numero*(-1)
        num_1 = num_positivo//100
        num_2 = (num_positivo//10)%10
        num_3 = num_positivo%10
        while (num_1==1 or num_2==1 or num_3==1):
            print("En el numero ingresado está el digito 1")
            break
    else:
        print("El numero ingresado NO es de tres digitos")
    
    
except ValueError:
    print("Error")