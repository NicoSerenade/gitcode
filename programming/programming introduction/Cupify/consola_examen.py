import cupify as c

def run_ganancia_neta_mensual():
    cantidad_kilometros = float(input("Entre la cantidad de kilometros: "))
    tarifa_kilometro = float(input("Entre la tarifa por kilometro: "))
    precio_galon = float(input("Entre el precio por galon: "))
    costo_mantenimiento = float(input("Entre el costo por mantenimiento: "))
    ganancia_neta_mes = c.ganancia_neta_mensual(cantidad_kilometros, tarifa_kilometro, precio_galon, costo_mantenimiento)
    print("La ganancia neta mensaul es de: ", ganancia_neta_mes)
    

def run_retorno_inversion():
    cantidad_kilometros = float(input("Entre la cantidad de kilometros: "))
    tarifa_kilometro = float(input("Entre la tarifa por kilometro: "))
    precio_galon = float(input("Entre el precio por galon: "))
    costo_mantenimiento = float(input("Entre el costo por mantenimiento: "))
    precio_veiculo = float(input("Entre el costo del vehiculo: "))

    meses_retorno = c.retorno_inversion(cantidad_kilometros, tarifa_kilometro, precio_galon, costo_mantenimiento, precio_veiculo)
    print("La cantidad de meses en recuperar la inversion es de: ", meses_retorno)
    
    
    
def run_app():
    print("Welcome!")
    run_retorno_inversion()
    run_ganancia_neta_mensual()
    
    
run_app()