import module as m

def run_peso_despues_de_un_mes()-> None:
    peso_kilos = float(input("Entre su peso en kilos: "))
    por_grasa = float(input("Entre su porcentaje de grasa en decimales: "))
    peso_posible_mes = m.peso_despues_de_un_mes(peso_kilos, por_grasa)
    print("El peso que puede alcanzar es:", peso_posible_mes)


def run_app()-> None:
    print("Welcome")
    run_peso_despues_de_un_mes()


run_app()
