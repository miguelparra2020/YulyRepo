numero = int(input("digite num"))

if (numero>3 and numero<54):
    var = (((2**numero)+(numero**2))/3)
    parte_decimal = abs(var) - abs(int(var))
    print(var, parte_decimal)
    if parte_decimal==0:
        print("Es primo")
    else:
        print("No es primo")
elif (numero==2 or numero==3):
    print("Primo")
elif (numero<=1):
    print("NO es primo")
else:
    print("NO es primo")