

def gramos_por_semana(peso: float, porcentaje_grasa: float) -> float:
    max_kcal_dia = 70
    s1 = peso * porcentaje_grasa
    s2 = max_kcal_dia * s1
    gramos_dia = s2/9
    gramos_semana = gramos_dia * 7
    return gramos_semana
    
def peso_despues_de_un_mes(peso: float, porcentaje_grasa: float) -> float:
    peso1_g = (peso*1000) - gramos_por_semana(peso, porcentaje_grasa)
    peso2_g = peso1_g - gramos_por_semana(peso1_g/1000, porcentaje_grasa)
    peso3_g = peso2_g - gramos_por_semana(peso2_g/1000, porcentaje_grasa)
    peso4_g = peso3_g - gramos_por_semana(peso3_g/1000, porcentaje_grasa)
    peso4_kilos = peso4_g/1000
    return round(peso4_kilos,2)