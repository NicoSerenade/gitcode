#MODULE OF LOGIC

def calcular_tarifa_distancia(distancia_recorrida: float) -> float:
    COSTO_KM = 500
    tarifa = distancia_recorrida * COSTO_KM
    return round(tarifa,2) #en pesos

def calcular_tarifa_tiempo(tiempo_transcurrido: float) -> float:
    COSTO_MIN = 250
    tarifa = tiempo_transcurrido * COSTO_MIN
    return round(tarifa,2) #en pesos

def calcular_tarifa_base(distancia_recorrida: float, tiempo_transcurrido: float) -> float:
    COBRO_BASE = 2700
    tarifa_distancia = calcular_tarifa_distancia(distancia_recorrida)
    tarifa_tiempo = calcular_tarifa_tiempo(tiempo_transcurrido)
    tarifa = COBRO_BASE + tarifa_distancia + tarifa_tiempo
    return round(tarifa, 2)


def calcular_tarifa_dinamica(distancia_recorrida: float, tiempo_transcurrido: float, indice_demanda: float) -> float:
    tarifa_base = calcular_tarifa_base(distancia_recorrida, tiempo_transcurrido)
    tarifa = tarifa_base * (1 + (indice_demanda/abs(1 + indice_demanda)))
    return round(tarifa,2)

def calcular_tarifa_total(distancia_recorrida: float, tiempo_transcurrido: float, indice_demanda: float) -> float:
    tarifa_dinamica = calcular_tarifa_dinamica(distancia_recorrida, tiempo_transcurrido, indice_demanda)
    IVA = 19/100
    tarifa = tarifa_dinamica * (1 + IVA)
    return round(tarifa,2)


def calcular_ganancia_conductor(distancia_recorrida: float, tiempo_transcurrido: float, indice_demanda: float, calificacion_conductor: int) -> float:
    PORCENTAJE_CONDUCTOR = 70/100
    FACTOR_BONIFICACION = 100
    tarifa_dinamica = calcular_tarifa_dinamica(distancia_recorrida, tiempo_transcurrido, indice_demanda)
    ganancia = (tarifa_dinamica * PORCENTAJE_CONDUCTOR) + (FACTOR_BONIFICACION * calificacion_conductor)
    return round(ganancia,2)

def ganancia_neta_mensual(cantidad_kilometros: float, tarifa_kilometro: float, precio_galon: float, costo_mantenimiento: float)->float:
    ingreso = cantidad_kilometros * tarifa_kilometro
    km_per_galon = ((1/0.08) * 1)
    gasto_galones = (cantidad_kilometros/km_per_galon) * precio_galon
    gasto_mantenimiento = (cantidad_kilometros//1000) * costo_mantenimiento
    gastos_totales = gasto_galones + gasto_mantenimiento
    ganancia_neta = ingreso - gastos_totales
    return ganancia_neta
    
def retorno_inversion(cantidad_kilometros: float, tarifa_kilometro: float, precio_galon: float, costo_mantenimiento: float, precio_veiculo: float)->float:
    ganancia_neta_mes = ganancia_neta_mensual(cantidad_kilometros, tarifa_kilometro, precio_galon, costo_mantenimiento)
    meses_retorno = precio_veiculo/ganancia_neta_mes
    return meses_retorno
