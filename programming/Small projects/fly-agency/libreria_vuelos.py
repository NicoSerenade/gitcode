# -*- coding: utf-8 -*-


def cargar_vuelos(ruta_archivo: str)->dict:
    """
    Esta función carga la información un conjunto de vuelos a partir de un archivo CSV.
    Los valores dentro del archivo deben estar separados por comas y estar en el siguiente orden:
        aerolinea,codigo_vuelo,origen,destino,distancia,salida,duracion,retraso
    La primera línea del archivo debe corresponder a los títulos de las columnas.
    Parámetros:
        ruta_archivo: la ruta del archivo que se quiere cargar
    Retorno:
        Un diccionario con la información de los vuelos.
        Las llaves del diccionario corresponderán a los códigos de los vuelos.
        Los valores del diccionario deben ser también diccionarios con las siguientes llaves:
            aerolinea,origen,destino,distancia,salida,duracion,retraso
    """
    vuelos = {}
    archivo = open(ruta_archivo)
    titulos = archivo.readline().split(",")

    linea = archivo.readline()
    while len(linea) > 0:
        datos = linea.split(",")
        codigo_vuelo = datos[1]
        vuelo = {}
        vuelo["aerolinea"] = datos[0]
        vuelo["origen"] = datos[2]
        vuelo["destino"] = datos[3]
        vuelo["distancia"] = datos[4]
        vuelo["salida"] = datos[5]
        vuelo["duracion"] = datos[6]
        vuelo["retraso"] = datos[7]
        vuelos[codigo_vuelo] = vuelo
        linea = archivo.readline()

    archivo.close()
    return vuelos

    
def aerolinea_con_mas_vuelos(vuelos):
    aero = ""
    aero_vuelos = 0
    aeros_count = {}
    for vuelo_code in vuelos:
        vuelo_local = vuelos[vuelo_code]
        aero_local = vuelo_local["aerolinea"]
        if not aero_local in aeros_count:
            aeros_count[aero_local] = 0
        aeros_count[aero_local] += 1
    
    for aero_code in aeros_count:
        value = aeros_count[aero_code]
        if value > aero_vuelos:
            aero_vuelos = value
            aero = aero_code
        
    return aero



vuelos = cargar_vuelos("data/vuelos.csv")
print(aerolinea_con_mas_vuelos(vuelos))