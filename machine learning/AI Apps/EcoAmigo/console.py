import logic as l

def run_get_advice():
    print("\n" + "="*60)
    question = input("Enter your water management question or scenario:\n")
    
    print("\nGenerating water management advice...")
    advice = l.get_water_advice(question)
    
    print("\nWater Management Advice:")
    print("-" * 40)
    print(advice)
    print("-" * 40)

def run_app():
    print("="*60)
    print("Welcome to the Water Management Advisor!")
    print("This advisor provides expert guidance on water conservation,")
    print("="*60)
    
    while True:
        run_get_advice()
        continue_choice = input("\nWould you like more water management advice? (y/n): ").lower()
        if continue_choice == "n":
            break

    print("\nThank you for using the Water Management Advisor!")
    print("Remember to conserve water - every drop counts!")

if __name__ == "__main__":
    run_app()
