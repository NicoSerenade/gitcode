import module as m

def run_invert_number() -> None:
    number = int(input("Enter the INT number about to invert: "))
    inverted_number = m.invert_number(number)
    print("The inverted number is:", inverted_number)

def run_app() -> None:
    print("Welcome to the inverter!")
    run_invert_number()

run_app()