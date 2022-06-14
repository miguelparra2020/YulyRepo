try:
    #Lista datos de pasajeros
    pasajeros = [
        ("Manuel Suarez", 19823451, "Liverpool"),
        ("Silvana Paredes",22709128, "Buenos Aires"), 
        ("Rosa Ortiz", 15123978, "Glasgow"), 
        ("Luciana Hernández", 38981374, "Lisboa")]
    #Lista datos de ciudades
    ciudades = [
        ("Buenos Aires", "Argentina"), 
        ("Glasgow", "Escocia"), 
        ("Lisboa", "Portugal"),
        ("Liverpool", "Inglaterra"), 
        ("Madrid", "España")]
    #Variables de iniciación
    ingresar_salir = 1
    menu_principal = 0
    menu_pasajeros = 0
    menu_ciudades = 0
    menu_validar_ciudad_pasajero = 0
    menu_cantidad_pasajeros_x_ciudad = 0
    menu_validar_pais_pasajero = 0
    menu_cantidad_pasajeros_x_pais = 0
    cont = 0

    #Ciclo de iniciación
    while ingresar_salir==1:
        print("")
        print("Bienvenido al sistema de pasajeros")
        print("")
        print("**************************************")
        print("")
        menu_principal = int(input("Para ingresar al menu principal por favor ingrese '1' \n"+
                                "Para salirse del programa marque '0'\n\n"))
        if menu_principal==1:
            ingresar_salir=0
        else:
            print("\nGracias por utilizar el sistema de Miguel Páez\n")
            break
    #Ciclo Menú Principal
    while menu_principal==1:
        #Opciones menú principal
        menu_opcion = int(input("\n\nEn este menú puede realizar lo siguiente: \n"+
                                "\n"+
                                "**********"+
                                "\n"+
                                "1- Para agregar pasajeros a la lista de viajeros, Ingresa '1'  \n" +
                                "2- Para agregar ciudades a la lista, Ingresa '2'  \n"+
                                "3- Para ver a que ciudad viaja un pasajero, Ingresa '3'  \n"+
                                "4- Para validar cuantos pasajeros viajan a una ciudad especifica, Ingresa '4'  \n"+
                                "5- Para ver a que país viaja un pasajero, Ingresa '5'  \n"+
                                "6- Para validar cuantos pasajeros viajan a un país especifico, Ingresa '6'  \n"+ 
                                "7- Para salir del programa, Ingresa '7'  \n\n" ))
        if menu_opcion==1:
            menu_pasajeros = 1
            menu_principal = 0
        elif menu_opcion==2:
            menu_ciudades = 1
            menu_principal = 0
        elif menu_opcion==3:
            menu_validar_ciudad_pasajero = 1
            menu_principal = 0
        elif menu_opcion==4:
            menu_cantidad_pasajeros_x_ciudad = 1
            menu_principal = 0
        elif menu_opcion==5:
            menu_validar_pais_pasajero = 1
            menu_principal = 0
        elif menu_opcion==6:
            menu_cantidad_pasajeros_x_pais = 1
            menu_principal = 0
        else:
            print("\nGracias por utilizar el sistema de Miguel Páez\n")
            break
        #Ciclo sub menú pasajeros    
        while menu_pasajeros==1:  
            #Opciones  sub menú pasajeros      
            print("\n En este menú podemos realizar: \n")
            print("\n ************************* \n")
            menu_pasajeros_opciones = int(input("1- Para ver los pasajeros registrados, ingresa '1' \n"+
                                                "2- Para registrar un nuevo pasajero, ingresa '2' \n"+
                                                "3- Para vovel al menú principal, ingresa '3' \n"+
                                                "4- Para salir del sistema, ingresa '4'\n\n"))
            if menu_pasajeros_opciones==1:
                print("\nEn el sistema de pasajeros tenemos registrado, ", len(pasajeros), "Pasajeros\n")
                for i in range(0,len(pasajeros)):
                    print(i,"Nombre del pasajero:",pasajeros[i][0],"\n   Cedula: ",pasajeros[i][1],"\n   Ciudad destino: ",pasajeros[i][2])
                menu_pasajeros_opciones = 0
            elif menu_pasajeros_opciones==2:
                pasajeros.append((str(input("Por favor ingrese el nombre del pasajero:         ")),int(input("Por favor ingrese el número de cedula del pasajero:        ")),str(input("Escoger la ciudad destino, Escribirla exactamente como aparece: \n"+str(ciudades)+"\n\n"))))
                menu_pasajeros_opciones==0
                print("\n Muchas gracias por registrar un nuevo pasajero")
            elif menu_pasajeros_opciones==3:
                menu_pasajeros=0
                menu_principal=1
            else:
                print("\nGracias por utilizar el sistema de Miguel Páez\n")
                break
        #Ciclo sub menú ciudades
        while menu_ciudades==1:
            #Opciones  sub menú ciudades
            print("\n En este menú podemos realizar: \n")
            print("\n ************************* \n")
            menu_ciudades_opciones = int(input("1- Para ver las ciudades registradas, ingresa '1' \n"+
                                                "2- Para registrar una nueva ciudad, ingresa '2' \n"+
                                                "3- Para vovel al menú principal, ingresa '3' \n"+
                                                "4- Para salir del sistema, ingresa '4'\n\n"))
            if menu_ciudades_opciones==1:
                print("\nEn el sistema de pasajeros tenemos registrado, ", len(ciudades), "Ciudades\n")
                for i in range(0,len(ciudades)):
                    print(i,"Nombre de la ciudad:",ciudades[i][0],"\n   País: ",ciudades[i][1])
                menu_ciudades_opciones = 0
            elif menu_ciudades_opciones==2:
                ciudades.append((str(input("Por favor ingrese el nombre de la nueva ciudad 'Primera MAYUSCULA':         ")),str(input("Por favor ingrese el nombre deL país 'Primera MAYUSCULA':         "))))
                menu_ciudades_opciones==0
                print("\n Muchas gracias por registrar una nueva ciudad")
            elif menu_ciudades_opciones==3:
                menu_ciudades=0
                menu_principal=1
            else:
                print("\nGracias por utilizar el sistema de Miguel Páez\n")
                break
        #Ciclo sub menú validación ciudad donde viaja un pasajero
        while menu_validar_ciudad_pasajero==1:
            print("\n en el sistema tenemos las siguientes cedulas registradas:\n")
            for i in range(0,len(pasajeros)):
                print(pasajeros[i][1])
            validar_celuda = int(input("Para buscar la ciudad destino del pasajero, por favor ingrese el numero de cedula\n\n"))
            for j in range(0,len(pasajeros)):
                if   validar_celuda in pasajeros[j]:
                    print("\nEl pasajero: ",pasajeros[j][0], "Tiene el destino a la ciudad de: ", pasajeros[j][2])     
            menu_validar_ciudad_pasajero = 0
            menu_principal = 1
        #Ciclo sub menú cantidad de pasajeros que van a una ciudad
        while menu_cantidad_pasajeros_x_ciudad==1:
            print("\n En el sistema tenemos las siguientes ciudades con destino de pasajeros:\n")
            for i in range(0,len(ciudades)):
                print(ciudades[i][0])
            validar_ciudad= str(input("Para buscar la cantidad de pasajeros que tienen destino a una ciudad, Ingresa correctamente el nombre de la ciudad\n\n"))
            
            for j in range(0,len(pasajeros)):
                if   validar_ciudad in pasajeros[j]:
                    cont +=1
            print("\nLa ciudad: ",validar_ciudad,"Tiene: ", cont, " Pasajeros")
                
            menu_cantidad_pasajeros_x_ciudad = 0
            menu_principal = 1
            cont = 0
        #Ciclo sub menú validación país donde viaja un pasajero
        while menu_validar_pais_pasajero==1:
            print("\n en el sistema tenemos las siguientes cedulas registradas:\n")
            for i in range(0,len(pasajeros)):
                print(pasajeros[i][1])
            validar_celuda = int(input("Para buscar el pais destino del pasajero, por favor ingrese el numero de cedula\n\n"))
            for j in range(0,len(pasajeros)):
                if   validar_celuda in pasajeros[j]:
                    print("\nEl pasajero: ",pasajeros[j][0], "Tiene el destino al país de:")
                    ciudad = pasajeros[j][2]
                    for k in range(0,len(ciudades)):
                        if   ciudad in ciudades[k]:
                            print(ciudades[k][1])
            menu_validar_pais_pasajero = 0
            menu_principal = 1
        #Ciclo sub menú cantidad de pasajeros que van a un país
        while menu_cantidad_pasajeros_x_pais==1:
            print("\n En el sistema tenemos los siguientes paises con destino de pasajeros:\n")
            for i in range(0,len(ciudades)):
                print(ciudades[i][1])
            validar_pais = str(input("Para buscar la cantidad de pasajeros que tienen destino a una ciudad, Ingresa correctamente el nombre de la ciudad\n\n"))
            
            for j in range(0,len(ciudades)):
                if   validar_pais in ciudades[j]:
                    validar_ciudad = ciudades[j][0]

            for k in range(0,len(pasajeros)):
                if   validar_ciudad in pasajeros[k]:
                    cont +=1
            print("\nEl país: ",validar_pais,"Tiene: ", cont, " Pasajeros")
                
            menu_cantidad_pasajeros_x_pais = 0
            menu_principal = 1
            cont = 0
except ValueError:
    print("Dato ingresado incorrecto")