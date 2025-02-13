import cupify as c

def run_calcular_tarifa_total()->None:
    distancia_recorrida = float(input("Digite la distancia recorrida: "))
    tiempo_transcurrido = float(input("Digite el tiempo transcurrido: "))
    indice_demanda = float(input("Digite el indice demanda: "))

    tarifa_total = c.calcular_tarifa_total(distancia_recorrida, tiempo_transcurrido, indice_demanda)

    print("La tarifa total es:", tarifa_total)

def run_app():
    print("Bienvenido, aqui podra calcular la tarifa total\n")
    run_calcular_tarifa_total()
    

run_app()
