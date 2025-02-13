import cupify as c

def run_calcular_ganancia_conductor():
    distancia_recorrida = float(input("Digite la distancia recorrida: "))
    tiempo_transcurrido = float(input("Digite el tiempo transcurrido: "))
    indice_demanda = float(input("Digite el indice demanda: "))
    calificacion_conductor = int(input("Digite la calificacion del conductor: "))

    ganancia_conductor = c.calcular_ganancia_conductor(distancia_recorrida, tiempo_transcurrido, indice_demanda, calificacion_conductor)
    
    print("La ganancia del conductor es:", ganancia_conductor)

def run_app():
    print("Bienvenido, aqui podra calcular la ganancia del conductor\n")
    run_calcular_ganancia_conductor()


run_app()