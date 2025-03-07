
import logic as l

def mostrar_sospechoso(sospechoso: dict) -> None:
    if sospechoso is not None and sospechoso != {}:
        codigo = sospechoso["codigo"]
        nombre = sospechoso["nombre"]
        edad = sospechoso["edad"]
        altura = sospechoso["altura"]
        pantalon = sospechoso["pantalon"]
        camisa = sospechoso["camisa"]
        usaba_gafas = sospechoso["usaba_gafas"]
        salon = sospechoso["salon"]
        coartada_confirmada = sospechoso["coartada_confirmada"]
        huellas_confirmadas = sospechoso["huellas_confirmadas"]
        
        print(
            "\nCódigo: {}\nNombre: {}\nEdad: {}\nAltura (en metros): {}\n"
            "Pantalón: {}\nCamisa: {}\nUsaba gafas: {}\n"
            "Salón: {}\nCoartada confirmada: {}\nHuellas confirmadas: {}".format(
                codigo, 
                nombre, 
                edad, 
                altura,
                pantalon, 
                camisa, 
                usaba_gafas,
                salon, 
                coartada_confirmada, 
                huellas_confirmadas
            )
        )
        
    else:
        print("\nError: No se ha proporcionado un diccionario válido con la información de un sospechoso.")

def mostrar_perfil_culpable(culpable: dict) -> None:
    if culpable is not None and culpable != {}:
        edad_estimada = culpable["edad_estimada"]
        altura_estimada = culpable["altura_estimada"]
        color_pantalon = culpable["color_pantalon"]
        color_camisa = culpable["color_camisa"]
        usaba_gafas = culpable["usaba_gafas"]
        salon_incidente = culpable["salon_incidente"]
        
        print(
            "\nEdad estimada: {}\nAltura estimada (en metros): {}\n"
            "Color de pantalón: {}\nColor de camisa: {}\n"
            "Usaba gafas: {}\nSalón en donde estaba: {}".format(
                edad_estimada, 
                altura_estimada,
                color_pantalon, 
                color_camisa,
                usaba_gafas, 
                salon_incidente
            )
        )

    else:
        print("\nError: No se ha proporcionado un diccionario válido con la información del culpable.")

def ejecutar_buscar_por_codigo(s1: dict, s2: dict, s3: dict, s4: dict) -> None:
    codigo = int(input("Ingrese el codigo del sospechoso: "))
    sospechoso = l.buscar_por_codigo(codigo,s1,s2,s3,s4)
    if sospechoso:
        mostrar_sospechoso(sospechoso)
    else:
        print("No se encontró un sospechoso con el código ingresado.")

def ejecutar_filtrar_sospechosos_por_ubicacion(perfil_culpable: dict, s1: dict, s2: dict, s3: dict, s4: dict) -> None:
    message = l.filtrar_sospechosos_por_ubicacion(perfil_culpable, s1, s2, s3, s4)
    if message != "Ninguno":
        print(f"Sospechosos en la ubicación del incidente (identificados por su código): {message}")
    else:
        print("No se encontraron sospechosos en la ubicación del incidente.")

def ejecutar_filtrar_sospechosos_por_vestimenta(perfil_culpable: dict, s1: dict, s2: dict, s3: dict, s4: dict) -> None:
    message = l.filtrar_sospechosos_por_vestimenta(perfil_culpable, s1, s2, s3, s4)
    if message != "Ninguno":
        print(f"Sospechosos por vestimenta (identificados por su código): {message}")
    else:
        print("No se encontraron sospechosos con vestimenta similar a la del presunto culpable.")
           
def ejecutar_filtrar_sospechosos_por_edad_altura(perfil_culpable: dict, s1: dict, s2: dict, s3: dict, s4: dict) -> None:
    message = l.filtrar_sospechosos_por_edad_altura(perfil_culpable, s1, s2, s3, s4)
    if message != "Ninguno":
        print(f"Sospechosos por edad y altura (identificados por su código): {message}")
    else:
        print("No se encontraron sospechosos con una edad y altura similares a las del presunto culpable.")     

def ejecutar_calcular_probabilidad_de_culpabilidad(perfil_culpable: dict, s1: dict, s2: dict, s3: dict, s4: dict) -> None:
    codigo = int(input("Ingrese el codigoo del sospechoso: "))
    if codigo == s1["codigo"] or codigo == s2["codigo"] or codigo == s3["codigo"] or codigo == s4["codigo"]:
        probabilidad = l.calcular_probabilidad_de_culpabilidad(codigo, perfil_culpable, s1, s2, s3, s4)
        print(f"La probabilidad de que el sospechoso con código: {codigo} sea el culpable es del: {int(probabilidad*100)}%")

    else:
        print("No se encontró ningún sospechoso con el código ingresado.")
        
def ejecutar_encontrar_sospechoso_con_mayor_probabilidad(perfil_culpable: dict, s1: dict, s2: dict, s3: dict, s4: dict) -> None:
    main_sospechoso = l.encontrar_sospechoso_con_mayor_probabilidad(perfil_culpable, s1, s2, s3, s4)
    mostrar_sospechoso(main_sospechoso)
    
def iniciar_aplicacion() -> None:
    sospechoso1 = l.crear_sospechoso(1, "Santiago", 25, 1.86, "Azul; Jeans; Largo", "Blanca; Cuello Redondo; Regular Fit", False, "ML-648", True, False)
    perfil_culpable = l.crear_perfil_culpable(22, 1.75, "Negro", "Morada", True, "ML-610")
    
    if sospechoso1 is not None and perfil_culpable is not None:
        sospechoso2 = l.crear_sospechoso(2, "Eric", 21, 1.75, "Negro; Bermuda; Largo", "Blanca; Cuello Polo; Slim Fit", True, "ML-610", False, False)
        sospechoso3 = l.crear_sospechoso(3, "Gabriel", 34, 1.99, "Negro; Bermuda; Largo", "Morada; Cuello Tortuga; Tailored Fit", True, "ML-410", True, False)
        sospechoso4 = l.crear_sospechoso(4, "Chu", 18, 1.65, "Negro; Bermuda; Corto", "Morada; Cuello Camisero; Oversize", True, "ML-610", False, True)

        BANDA = "*" * 60
        print("\n", BANDA, "\nPerfil del presunto sospechoso según Séneca:", sep='')
        print(BANDA)
        mostrar_perfil_culpable(perfil_culpable)
        print(BANDA, "\n")
        
        print(BANDA, "\nInformación de los 4 sospechosos:")
        print(BANDA)

        print("\nSospechoso 1 -> s1:\n")
        mostrar_sospechoso(sospechoso1)
        
        RAYA = "-" * 50
        print(RAYA, "\n\nSospechoso 2 -> s2:\n")
        mostrar_sospechoso(sospechoso2)
        
        print(RAYA, "\n\nSospechoso 3 -> s3:\n")
        mostrar_sospechoso(sospechoso3)
        
        print(RAYA, "\n\nSospechoso 4 -> s4:\n")
        mostrar_sospechoso(sospechoso4)
        
        print("\n", BANDA, "\n", sep='')
        
        ejecutando = True   
        
    else:
        print("\nError: Primero debe implementar las funciones crear_sospechoso() y crear_perfil_culpable() en: cupi_detectives.py")
        ejecutando = False
    
    while ejecutando:
        ejecutando = mostrar_menu_aplicacion(perfil_culpable, sospechoso1, sospechoso2, sospechoso3, sospechoso4)        
        
        if ejecutando:
            input("\nPresione cualquier tecla para continuar...")

def mostrar_menu_aplicacion(perfil_culpable: dict, sospechoso1: dict, sospechoso2: dict, sospechoso3: dict, sospechoso4: dict) -> bool:
    """
    Muestra el menú de la aplicación CupiDetectives y ejecuta la acción correspondiente según la opción seleccionada por el usuario.
    """
    print("\nMenú:")
    print(" 1 - Buscar sospechoso por código")
    print(" 2 - Filtrar sospechosos por ubicación")
    print(" 3 - Filtrar sospechosos por vestimenta")
    print(" 4 - Filtrar sospechosos por edad y altura")
    print(" 5 - Calcular probabilidad de culpa de un sospechoso")
    print(" 6 - Buscar sospechoso más probable")
    print(" 7 - Salir\n")
    
    opcion_elegida = input("Ingrese la opción que desea ejecutar: ").strip()
    
    BANDA = "*" * 80
    print("\n", BANDA, "\n", sep='')

    continuar_ejecutando = True
    
    if opcion_elegida == "1":
        ejecutar_buscar_por_codigo(sospechoso1, sospechoso2, sospechoso3, sospechoso4)
    elif opcion_elegida == "2":
        ejecutar_filtrar_sospechosos_por_ubicacion(perfil_culpable, sospechoso1, sospechoso2, sospechoso3, sospechoso4)
    elif opcion_elegida == "3":
        ejecutar_filtrar_sospechosos_por_vestimenta(perfil_culpable, sospechoso1, sospechoso2, sospechoso3, sospechoso4)
    elif opcion_elegida == "4":
        ejecutar_filtrar_sospechosos_por_edad_altura(perfil_culpable, sospechoso1, sospechoso2, sospechoso3, sospechoso4)
    elif opcion_elegida == "5":
        ejecutar_calcular_probabilidad_de_culpabilidad(perfil_culpable, sospechoso1, sospechoso2, sospechoso3, sospechoso4)
    elif opcion_elegida == "6":
        print("Información del sospechoso más probable:")
        ejecutar_encontrar_sospechoso_con_mayor_probabilidad(perfil_culpable, sospechoso1, sospechoso2, sospechoso3, sospechoso4)
        print("\nFINAL FELIZ: \nLos CupiDetectives corroboraron que el principal sospechoso, únicamente llevó a Edouardinho a un SPA,\ny nunca tuvo una mala intención :) :) :)")
    elif opcion_elegida == "7":
        continuar_ejecutando = False
    else:
        print("Opción inválida. Por favor intente de nuevo.")
    
    return continuar_ejecutando

if __name__ == "__main__":
    iniciar_aplicacion()    