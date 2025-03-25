import logic as l

def run_get_advice():
    print("\n" + "="*60)
    question = input("Preguntale a EcoAmigo:\n")
    
    print("\nGenerando respuesta...")
    advice = l.get_water_advice(question)
    
    print("\nWater Management Advice:")
    print("-" * 40)
    print(advice)
    print("-" * 40)

def run_app():
    print("="*60)
    print("Bienvenido a EcoAmigo!")
    print("Este consultor ofrece orientación experta sobre la conservación del agua en bogotá.")
    print("="*60)
    
    while True:
        run_get_advice()
        continue_choice = input("\nTienes otra inquietud? (y/n): ").lower()
        if continue_choice == "n":
            break

    print("\nGracias por usar a EcoAmigo!")
    print("Recuerda conservar el agua: cada gota cuenta!")

if __name__ == "__main__":
    run_app()
