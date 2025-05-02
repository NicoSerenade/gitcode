def cargar_vuelos(archivo: str) -> dict:
    vuelos = {}
    archivo = open(archivo, "r", encoding="utf-8")
    titulos = archivo.readline().strip()
    linea = archivo.readline().strip()

    while len(linea) > 0:
        datos = linea.split(",") #list of substrings separated at each ","

        aerolinea = datos[0].strip()
        vuelo = {}
        vuelo["codigo"] = datos[1].strip()
        vuelo["origen"] = datos[2].strip()
        vuelo["destino"] = datos[3].strip()
        vuelo["disctancia"] = int(datos[4])
        vuelo["salida"] = int(datos[5])
        vuelo["duracion"] = int(datos[6])
        vuelo["retraso"] = int(datos[7])
        
        if not aerolinea in vuelos:
            vuelos[aerolinea] = []
        vuelos[aerolinea].append(vuelo)

        linea = archivo.readline().strip()

    archivo.close()
    return vuelos

def buscar_vuelo(vuelos, codigo_vuelo):
    aerolinea = codigo_vuelo[0:2]
    vuelo = None
    iteration = 0
    while not vuelo and iteration < len(vuelos[aerolinea]):
        if vuelos[aerolinea][iteration]["codigo"] == codigo_vuelo:
            vuelo = vuelos[aerolinea][iteration]
        iteration += 1
    return vuelo

def vuelo_mas_largo_aerolinea(vuelos, aerolinea):
    vuelos_aerolinea = vuelos[aerolinea]
    vuelo_code = ""
    duracion = 0
    for vuelo in vuelos_aerolinea:
        if vuelo["duracion"] > duracion:
            duracion = vuelo["duracion"]
            vuelo_code = vuelo["codigo"]
    return vuelo_code

def aerolinea_con_mas_vuelos(vuelos):
    aero = ""
    aero_count = 0
    for aero_code in vuelos:
        aero_vuelos = vuelos[aero_code]
        if len(aero_vuelos) > aero_count:
            aero_count = len(aero_vuelos)
            aero = aero_code
    return aero



#CONSOLE
vuelos = cargar_vuelos("data/vuelos.csv")
print(aerolinea_con_mas_vuelos(vuelos))