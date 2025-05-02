#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CupiTube
"""

import cupitube as ct


###### Funciones auxiliares (NO MODIFICAR):
    
# Función auxiliar que muestra la información de un CupiTuber
def mostrar_cupituber(cupituber: dict) -> None:
    """
    Muestra la información de un CupiTuber.
    
    Parámetros:
        cupituber (dict): Diccionario con la información del CupiTuber.
    """
    print("\n")
    print("#" * 50)
    
    print((
        "\nNombre: {}\n"
        "Ranking: {}\n"
        "Suscriptores: {}\n"
        "Visitas de videos: {}\n"
        "Cantidad de videos: {}\n"
        "Categoría: {}\n"
        "Año de inicio: {}\n"
        "Tipo de monetización: {}\n"
        "Descripción: {}\n"
    ).format(
        cupituber["cupituber"], cupituber["rank"], cupituber["subscribers"],
        cupituber["video_views"], cupituber["video_count"], cupituber["category"],
        cupituber["started"], cupituber["monetization_type"], cupituber["description"]
    ))
    
    print("#" * 50)

# Función auxiliar que muestra la información de múltiples CupiTubers
def mostrar_cupitubers(cupitubers: list) -> None:
    """
    Muestra la información de una lista de CupiTubers.
    
    Parámetros:
        cupitubers (list): Lista de diccionarios con la información de los CupiTubers.
    """
    print("\nCupiTubers encontrados:")
    print("-" * 50)
    
    for cupituber in cupitubers:
        mostrar_cupituber(cupituber)

    print("-" * 50)
    
# Función auxiliar que muestra los países de CupiTubers en una categoría específica.
def mostrar_paises(paises: list) -> None:
    """ 
    Muestra los países que tienen CupiTubers en una categoría específica.
    
    Parámetros:
        paises (list): Lista de nombres de países.
    """
    print("-" * 50)
    
    for pais in paises:
        print(pais)
    
    print("-" * 50)
###### Fin de las funciones auxiliares



# Funciones a implementar (solo aquellas con TODOs):

def ejecutar_buscar_por_categoria_y_rango_suscriptores(cupitube: dict) -> None:
    """
    Muestra los CupiTubers que pertenecen a la categoría dada y cuyo número de suscriptores se encuentre dentro del rango especificado.
    Ya se provee la implementación completa de esta función y no se requiere ningún cambio.
               
    Parámetros:
        cupitube (dict): Diccionario con la información de los CupiTubers.
        
    Se debe pedir al usuario la categoría, y el mínimo y el máximo del rango de suscriptores.    
    
    Hay 2 casos posibles:
        - Si no se encuentra ningún CupiTuber que cumpla con los criterios, el mensaje es:
            - "No se encontraron CupiTubers que cumplan con los criterios."
        
        - Caso contrario, debe usar la función auxiliar: mostrar_cupitubers() para mostrar a todos los CupiTubers que cumplan con los criterios.
    """
    categoria = input("Ingrese la categoría: ")
    minimo = int(input("Ingrese el mínimo de suscriptores: "))
    maximo = int(input("Ingrese el máximo de suscriptores: "))
    
    cupitubers = ct.buscar_por_categoria_y_rango_suscriptores(cupitube, minimo, maximo, categoria)
    
    if cupitubers != []:
        mostrar_cupitubers(cupitubers)
    else:
        print("No se encontraron CupiTubers que cumplan con los criterios.")


def ejecutar_buscar_cupitubers_por_pais_categoria_monetizacion(cupitube: dict) -> None:
    """ 
    Muestra los CupiTubers de un país que pertenezcan a una categoría específica y tengan una monetización en particular.

    Parámetros:
        cupitube (dict): Diccionario con la información de los CupiTubers.

    Se debe pedir al usuario el país, la categoría y el tipo de monetización.
    Por favor recuerde que el nombre un país en el dataset inicia con letra mayúscula, por ejemplo: "India"

    Hay 2 casos posibles:
        - Si no se encuentra ningún CupiTuber que cumpla con los criterios, el mensaje es:
            - "No se encontraron CupiTubers que cumplan con los criterios."

        - De lo contrario, el mensaje tiene el siguiente formato:
            - "Los CupiTubers de [X] que pertenecen a la categoría [Y] y tienen monetización [Z] son:"

            Nota: Aquí, los corchetes se usan para indicar la ubicación para la información definida a continuación:

            Donde:
                - [X] es el nombre del país ingresado por el usuario.
                - [Y] es la categoría ingresada por el usuario.
                - [Z] es el tipo de monetización ingresado por el usuario.
                
           - Luego, use la función auxiliar mostrar_cupitubers() para mostrar la información de los CupiTubers encontrados.
    """
    #TODO 10: Implemente la función tal y como se describe en la documentación.
    pais = input("Ingrese el país: ")
    categoria = input("Ingrese la categoría: ")
    monetizacion = input("Ingrese el tipo de monetización: ")
    
    cupitubers = ct.buscar_cupitubers_por_pais_categoria_monetizacion(cupitube, pais, categoria, monetizacion)
    
    if cupitubers != []:
        print("Los CupiTubers de " + pais + " que pertenecen a la categoría " + categoria + " y tienen monetización " + monetizacion + " son:")
        mostrar_cupitubers(cupitubers)
    else:
        print("No se encontraron CupiTubers que cumplan con los criterios.")

        
def ejecutar_buscar_cupituber_mas_antiguo(cupitube: dict) -> None:
    """
    Muestra el CupiTuber más antiguo con base en la fecha de inicio (started).
    
    Parámetros:
        cupitube (dict): Diccionario con la información de los CupiTubers.
        
    No hay datos que solicitar al usuario.
    
    El mensaje debe tener el siguiente formato:
        - "El CupiTuber más antiguo es [X] y empezó en [Y]."

        Nota: Aquí, los corchetes se usan para indicar la ubicación para la información definida a continuación:
        
        Donde:
            - [X] es el nombre del CupiTuber.
            - [Y] es la fecha en la que empezó a publicar videos (started) en formato YYYY-MM-DD.
    """    
    #TODO 11: Implemente la función tal y como se describe en la documentación.
    cupituber = ct.buscar_cupituber_mas_antiguo(cupitube)
    print("El CupiTuber más antiguo es " + cupituber["cupituber"] + " y empezó en " + cupituber["started"] + ".")


def ejecutar_obtener_visitas_por_categoria(cupitube: dict) -> None:
    """ 
    Muestra el número total de visitas (video_views) acumuladas para una categoría dada de CupiTubers.
    
    Parámetros:
        cupitube (dict): Diccionario con la información de los CupiTubers.
        
    Se debe pedir al usuario la categoría de CupiTubers.

    El mensaje debe tener el siguiente formato:    
        - "El total de visitas para la categoría [X] es: [Y]."

        Nota: Aquí, los corchetes se usan para indicar la ubicación para la información definida a continuación:
        
        Donde:
            - [X] es el nombre de la categoría ingresada por el usuario.
            - [Y] es el número total de visitas acumuladas para la categoría. Este número puede ser cero.
    """
    #TODO 12: Implemente la función tal y como se describe en la documentación.
    categoria = input("Ingrese la categoría: ")
    visitas = ct.obtener_visitas_por_categoria(cupitube, categoria)
    print("El total de visitas para la categoría " + categoria + " es: " + str(visitas) + ".")


def ejecutar_obtener_categoria_con_mas_visitas(cupitube: dict) -> None:
    """ 
    Muestra la categoría con el mayor número de visitas (video_views) acumuladas.
    
    Parámetros:
        cupitube (dict): Diccionario con la información de los CupiTubers.
        
    No hay datos que solicitar al usuario.
        
    El mensaje debe tener el siguiente formato:
        - "La categoría con más visitas es [X] con [Y] visitas."

        Nota: Aquí, los corchetes se usan para indicar la ubicación para la información definida a continuación:
        
        Donde:
            - [X] es el nombre de la categoría con el mayor número de visitas acumuladas.
            - [Y] es el número total de visitas acumuladas para la categoría con más visitas.
    """
    #TODO 13: Implemente la función tal y como se describe en la documentación.
    dict_category = ct.obtener_categoria_con_mas_visitas(cupitube)
    categoria = dict_category["categoria"]
    visitas = dict_category["visitas"]
    print("La categoría con más visitas es " + categoria + " con " + str(visitas) + " visitas.")
    

def ejecutar_crear_correo_para_cupitubers(cupitube: dict) -> None:
    """ 
    Ejecuta la función de crear correos para CupiTubers.
    Ya se provee la implementación completa de esta función y no se requiere ningún cambio.
    
    Parámetros:
        cupitube (dict): Diccionario con la información de los CupiTubers.
        
    A modo de ejemplo, se muestra el correo creado para el primer CupiTuber del país 'USA'.
    
    El mensaje tiene el siguiente formato:
        - "El correo para el primer Cupituber de 'USA' con nombre '[X]' es: [Y]."

        Nota: Aquí, los corchetes se usan para indicar la ubicación para la información definida a continuación:
        
        Donde:
            - [X] es el nombre del CupiTuber.
            - [Y] es el correo creado.
    """
    if "USA" in cupitube and cupitube["USA"] != [] and cupitube["USA"][0] is not None:
        ct.crear_correo_para_cupitubers(cupitube)
        cupituber = cupitube["USA"][0]
        print("El correo para el primer Cupituber de 'USA' con nombre '" + cupituber["cupituber"] + "' es: " + cupituber["correo"] + ".")
        

def ejecutar_recomendar_cupituber(cupitube: dict) -> None:
    """ 
    Ejecuta la función de  que recomienda al primer CupiTuber que cumpla con todos los criterios de búsqueda especificados:
    - Pertenece a la categoría con más visitas totales.
    - Tiene un número de suscriptores dentro del rango especificado.
    - Ha publicado al menos la cantidad mínima de videos indicada.
    - Ha comenzado a publicar dentro del rango de fechas especificado.
    - Contiene la palabra clave indicada como parte de la descripción (sin distinguir entre mayúsculas/minúsculas).
        
    Parámetros:
        cupitube (dict): Diccionario de países con la información de los CupiTubers.
        
    Se debe pedir al usuario la siguiente información:
        - El límite inferior del rango de suscriptores.
        - El límite superior del rango de suscriptores.
        - El límite inferior del rango de fechas. El formato de ingreso debe ser: YYYY-MM-DD
        - El límite superior del rango de fechas. El formato de ingreso debe ser: YYYY-MM-DD
        - La cantidad mínima de videos requerida.
        - La palabra clave que se desea sea parte de la descripción.
          - La palabra clave no puede ser una cadena vacía.
        
    El mensaje debe tener el siguiente formato:
    
    Hay dos casos posibles:
        - Si no se encuentra un CupiTuber que cumpla con los criterios o la palabra clave dada es una cadena vacía, el mensaje es:
            - "No se encontró un CupiTuber que cumpla con los criterios."

        - Caso contrario, proceda así:
            - Primero imprima el encabezado: "El Cupituber recomendado tiene la siguiente información:"
              - Luego, use la función auxiliar mostrar_cupituber() para mostrar la información del CupiTuber recomendado.
    """
    #TODO 14: Implemente la función tal y como se describe en la documentación.
    suscriptores_min = int(input("Ingrese el límite inferior del rango de suscriptores: "))
    suscriptores_max = int(input("Ingrese el límite superior del rango de suscriptores: "))
    fecha_min = input("Ingrese el límite inferior del rango de fechas (YYYY-MM-DD): ")
    fecha_max = input("Ingrese el límite superior del rango de fechas (YYYY-MM-DD): ")
    video_min = int(input("Ingrese la cantidad mínima de videos: "))
    palabra_clave = input("Ingrese la palabra clave para la descripción: ").strip()
    
    message2 = "No se encontró un CupiTuber que cumpla con los criterios."
    if palabra_clave == "":
        print(message2)
  
    else:  
        cupituber = ct.recomendar_cupituber(cupitube, suscriptores_min, suscriptores_max, fecha_min, fecha_max, video_min, palabra_clave)
    
        if cupituber:
            print("El Cupituber recomendado tiene la siguiente información:")
            mostrar_cupituber(cupituber)
        else:
            print(message2)
    
    
def ejecutar_paises_por_categoria(cupitube: dict) -> None:
    """ 
    Ejecuta la función que obtiene el diccionario de los países por categoría.
    Ya se provee la implementación completa de esta función y no se requiere ningún cambio.
    
    Parámetros:
        cupitube (dict): Diccionario con la información de los CupiTubers.
        
    Se debe pedir al usuario una categoría y mostrar los países que tienen CupiTubers en esa categoría.
    
    Hay dos casos posibles:
        - Si no se encuentra la categoría, el mensaje es:
            - "La categoría ingresada no existe en los datos."
    
        - Caso contrario, el mensaje debe tener el siguiente formato:
            - "Los países con CupiTubers en la categoría [X] son:"
        
            Nota: Aquí, los corchetes se usan para indicar la ubicación para la información definida a continuación:
        
            Donde:
                - [X] es el nombre de la categoría ingresada por el usuario.
            
        - Luego, use la función auxiliar mostrar_paises() para mostrar la información de los países encontrados.
    """
    estructura = ct.paises_por_categoria(cupitube)
    
    categoria = input("Ingrese la categoría: ")
    
    if categoria != "" and categoria in estructura:
        paises = estructura[categoria]
        if paises != {} and paises is not None:
            print("\nLos países con CupiTubers en la categoría " + categoria + " son:")
            mostrar_paises(paises)
    else:
        print("La categoría ingresada no existe en los datos.")


###### Funciones del ménu (NO MODIFICAR):
def iniciar_aplicacion() -> None:
    """
    Función principal de la aplicación.
    """
    ejecutando = False
    archivo = input("Ingrese el nombre del archivo de datos o presione Enter si su archivo se llama cupitube.csv: ")
    
    if archivo == "":
        archivo = "cupitube.csv"
        
    estados = ct.cargar_cupitube(archivo)
    if estados != {} and estados is not None:
        ejecutando = True
        print("#" * 50)
        print("¡Bienvenido a la aplicación de CupiTube!")
        print("#" * 50)
    
        while ejecutando:
            ejecutando = mostrar_menu_aplicacion(estados)
            if ejecutando:
                input("Presione Enter para continuar...")
    else:
        print("\nError: No se ha podido cargar el archivo. \nRevise su implementación de la función: cargar_cupitube() en cupitube.py")
      
            
# Función para mostrar el menú de la aplicación:
def mostrar_menu_aplicacion(cupitube: dict) -> bool:
    """ 
    Muestra el menú de la aplicación y ejecuta la opción seleccionada por el usuario.
    """
    print("\nMenú de opciones:")
    print("1. Buscar CupiTubers por categoría y rango de suscriptores.")
    print("2. Buscar CupiTubers por país, categoría y monetización.")
    print("3. Buscar CupiTuber más antiguo.")
    print("4. Obtener visitas para una categoría.")
    print("5. Obtener categoría con más visitas.")
    print("6. Crear correo para CupiTubers.")
    print("7. Recomendar un CupiTuber.")
    print("8. Obtener países por categoría.")
    print("9. Salir.")

    opcion_elegida = input("Ingrese la opción que desea ejecutar: ").strip()

    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_buscar_por_categoria_y_rango_suscriptores(cupitube)
    elif opcion_elegida == "2":
        ejecutar_buscar_cupitubers_por_pais_categoria_monetizacion(cupitube)
    elif opcion_elegida == "3":
        ejecutar_buscar_cupituber_mas_antiguo(cupitube)
    elif opcion_elegida == "4":
        ejecutar_obtener_visitas_por_categoria(cupitube)
    elif opcion_elegida == "5":
        ejecutar_obtener_categoria_con_mas_visitas(cupitube)
    elif opcion_elegida == "6":
        ejecutar_crear_correo_para_cupitubers(cupitube)
    elif opcion_elegida == "7":
        ejecutar_recomendar_cupituber(cupitube)
    elif opcion_elegida == "8":
        ejecutar_paises_por_categoria(cupitube)
    elif opcion_elegida == "9":
        print("\n¡Gracias por usar la aplicación de CupiTube!")
        continuar_ejecutando = False
    else:
        print("Opción inválida. Por favor inténtelo de nuevo.")

    return continuar_ejecutando
###### Fin de las funciones del menú


# Punto de entrada de la aplicación
if __name__ == "__main__":
    iniciar_aplicacion()