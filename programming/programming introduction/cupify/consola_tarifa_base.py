import cupify as c

def run_calcular_tarifa_base()->None:
    distancia_recorrida = float(input("Digite la distancia recorrida: "))
    tiempo_transcurrido = float(input("Digite el tiempo transcurrido: "))

    tarifa_base = c.calcular_tarifa_base(distancia_recorrida, tiempo_transcurrido)
    
    print("La tarifa base es:", tarifa_base)
    

def run_app()->None:
    print("Bienvenido, aqui podra calcular la tarifa base\n")
    run_calcular_tarifa_base()


run_app()
