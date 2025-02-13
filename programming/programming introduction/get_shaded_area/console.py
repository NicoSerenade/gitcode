import module as m

def run_get_shaded_area():
    square_side = float(input("Enter the lenght of the square's side in meters: "))
    shaded_area = m.get_shaded_area(square_side)
    print("The shaded area for an square with sides of",square_side,"meters is:",shaded_area,"m^2")

def run_app():
    print("Welcome to get the shaded area!")
    run_get_shaded_area()


run_app()