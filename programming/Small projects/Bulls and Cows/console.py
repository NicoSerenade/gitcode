import logic as l

def run_main():
    play_again = None
    while play_again != "n":
        current_game = False
        bulls = 0
        rules = input("Do you want to see the rules?\n(y/n) ").lower()
        while True:
            if rules == "y": 
                print("Your goal is to guess a secret 4-digit number with all unique digits. \nFor each guess, you'll get hints: \n'Bull' means a correct digit in the right spot \n'Cow' means a correct digit but in the wrong spot. \nKeep guessing until you get 4 Bulls and crack the code! \nRemember, no repeated digits in guesses. \nGood luck and have fun! 🐂🐄")
                understood = input("Do you understand?\n(y/n) ")
                if understood == "y":
                    break
                else:
                    print("Wise up man, it is quite simple")
            else:
                break
      
        while bulls != 4:
            guess = input("Enter your 4 digit guess: ")
            if not current_game:
                secret_number = l.get_secret_number()
            bulls, cows = l.main(secret_number, guess)
            print(f"You got {bulls} BULLS and {cows} COWS")
            current_game = True

        print("You have won!")  
        play_again = input("Do you want to play again?\n(y/n) ").lower()

    print("Thank you for playing!")
            
    

def run_app():
    print("Welcome to Bulls and Cows!")
    run_main()

run_app()