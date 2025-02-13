def calcular_horario_llegada(hora_salida: int, minuto_salida: int, segundo_salida: int, duracion_horas: int, duracion_minutos: int, duracion_segundos: int)->str:
    horas_llegada = 0
    minutos_llegada = 0
    segundos_llegada = 0

    hora_llegada += hora_salida + duracion_horas
    minutos_llegada += minuto_salida + duracion_minutos
    segundos_llegada += segundo_salida + duracion_segundos

    quotient, remainder = divmod(segundos_llegada, 60)
    segundos_llegada = remainder
    minutos_llegada += quotient

    quotient, remainder = divmod(minutos_llegada, 60)
    minutos_llegada = remainder
    horas_llegada += quotient

    '''quotient, remainder = divmod(horas_llegada, 24)
    horas_llegada = remainder
    horas_llegada += quotient'''

    hora_llegada = []
    hora_llegada.append(horas_llegada)
    hora_llegada.append(minutos_llegada)
    hora_llegada.append(segundos_llegada)

    hora_llegada_str = ":".join(map(str, hora_llegada))

    return hora_llegada_str 

print(calcular_horario_llegada(1,59,59,1,2,2))


