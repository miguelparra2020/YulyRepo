# 12. Leer dos números enteros de dos dígitos y determinar si tienen dígitos comunes.
try:
    numero_1 = int(input("Por favor ingrese el primer número de dos digitos "))
    numero_2 = int(input("Por favor ingrese el segundo número de dos digitos "))

    if ((numero_1 >=10 and numero_1 <=99) and (numero_2 >=10 and numero_2 <=99)):
        num_3 = numero_1//10
        num_4 = numero_1%10
        num_5 = numero_2//10
        num_6 = numero_2%10
        if (num_3 == num_5):
            print("Del los numeros ingresados:", numero_1,"y",numero_2,"El primer digito:",num_3,
            "Es común con el primer digito:",num_5)
        elif (num_3 == num_6):
            print("Del los numeros ingresados:", numero_1,"y",numero_2,"El primer digito:",num_3,
            "Es común con el segundo digito:",num_6)
        elif (num_4 == num_5):
            print("Del los numeros ingresados:", numero_1,"y",numero_2,"El segundo digito:",num_4,
            "Es común con el primer digito:",num_5)
        elif (num_4 == num_6):
            print("Del los numeros ingresados:", numero_1,"y",numero_2,"El segundo digito:",num_4,
            "Es común con el segundo digito:",num_6)
        else:
            print("de los numeros ingresados NO tienen digitos comunes")
    elif ((numero_1 >=-99 and numero_1 <=-10) and (numero_2 >=-99 and numero_2 <=-10)):
        num_positivo_1 = numero_1*(-1)
        num_positivo_2 = numero_2*(-1)
        num_3 = num_positivo_1//10
        num_4 = num_positivo_1%10
        num_5 = num_positivo_2//10
        num_6 = num_positivo_2%10
        if (num_3 == num_5):
            print("Del los numeros ingresados:", numero_1,"y",numero_2,"El primer digito:",num_3,
            "Es común con el primer digito:",num_5)
        elif (num_3 == num_6):
            print("Del los numeros ingresados:", numero_1,"y",numero_2,"El primer digito:",num_3,
            "Es común con el segundo digito:",num_6)
        elif (num_4 == num_5):
            print("Del los numeros ingresados:", numero_1,"y",numero_2,"El segundo digito:",num_4,
            "Es común con el primer digito:",num_5)
        elif (num_4 == num_6):
            print("Del los numeros ingresados:", numero_1,"y",numero_2,"El segundo digito:",num_4,
            "Es común con el segundo digito:",num_6)
        else:
            print("de los numeros ingresados NO tienen digitos comunes")
    elif ((numero_1 >=-99 and numero_1 <=-10) and (numero_2 >=10 and numero_2 <=10)):
        num_positivo_1 = numero_1*(-1)
        
        num_3 = num_positivo_1//10
        num_4 = num_positivo_1%10
        num_5 = numero_2//10
        num_6 = numero_2%10
        if (num_3 == num_5):
            print("Del los numeros ingresados:", numero_1,"y",numero_2,"El primer digito:",num_3,
            "Es común con el primer digito:",num_5)
        elif (num_3 == num_6):
            print("Del los numeros ingresados:", numero_1,"y",numero_2,"El primer digito:",num_3,
            "Es común con el segundo digito:",num_6)
        elif (num_4 == num_5):
            print("Del los numeros ingresados:", numero_1,"y",numero_2,"El segundo digito:",num_4,
            "Es común con el primer digito:",num_5)
        elif (num_4 == num_6):
            print("Del los numeros ingresados:", numero_1,"y",numero_2,"El segundo digito:",num_4,
            "Es común con el segundo digito:",num_6)
        else:
            print("de los numeros ingresados NO tienen digitos comunes")
    elif ((numero_1 >=10 and numero_1 <=99) and (numero_2 >=-99 and numero_2 <=10)):
        um_positivo_2 = numero_2*(-1)
        
        num_3 = numero_1//10
        num_4 = numero_1%10
        num_5 = um_positivo_2//10
        num_6 = um_positivo_2%10
        if (num_3 == num_5):
            print("Del los numeros ingresados:", numero_1,"y",numero_2,"El primer digito:",num_3,
            "Es común con el primer digito:",num_5)
        elif (num_3 == num_6):
            print("Del los numeros ingresados:", numero_1,"y",numero_2,"El primer digito:",num_3,
            "Es común con el segundo digito:",num_6)
        elif (num_4 == num_5):
            print("Del los numeros ingresados:", numero_1,"y",numero_2,"El segundo digito:",num_4,
            "Es común con el primer digito:",num_5)
        elif (num_4 == num_6):
            print("Del los numeros ingresados:", numero_1,"y",numero_2,"El segundo digito:",num_4,
            "Es común con el segundo digito:",num_6)
        else:
            print("de los numeros ingresados NO tienen digitos comunes")
    else:
        print("Los numeros ingresados son incorrectos, recuerda que debe ser de dos digitos")
except ValueError: 
    print("El dato ingresado es Erroneo")