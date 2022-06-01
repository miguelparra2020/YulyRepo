# 10.Ejemplo
try:
    ingresar = int(input("ingrese al ciclo con un numero positivo"))
    while ingresar>0:
        numero = int(input("por favor ingrese el numero a evaluar"))
        if numero<0:
            print("Numero Negativo")
        elif numero>0:
            print("Numero Positivo")
        else:
            print("Se reinicia la solicitud")
            break
except ValueError:
    print("El dato ingresado es Erroneo")