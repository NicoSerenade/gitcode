import cupify as c

def run_calcular_tarifa_dinamica()->None:
    distancia_recorrida = float(input("Digite la distancia recorrida: "))
    tiempo_transcurrido = float(input("Digite el tiempo transcurrido: "))
    indice_demanda = float(input("Digite el indice demanda: "))

    tarifa_dinamica = c.calcular_tarifa_dinamica(distancia_recorrida, tiempo_transcurrido, indice_demanda)

    print("La tarifa dinamica es:", tarifa_dinamica)

def run_app():
    print("Bienvenido, aqui podra calcular la tarifa dinamica\n")
    run_calcular_tarifa_dinamica()


run_app()
