import random
import sys

def user_input():
    while True:
        try:  
            guess_num = int(input("Enter your guess: "))
            if guess_num in range(1, 101):
                return guess_num
            else:
                print("Invalid choice")
        except ValueError:
            print('Invalid choice')
        
def check_num(guess_num, num, attempts):
    if guess_num == num:
        print(f"You're spot on, it only took you {attempts} attempts!")
        return True
    elif guess_num < num:
            print("Too low")
    else:
        print("Too high")
        
        
def restart():
    while True:
        again = input("do you want to play again? (y/n): ").lower()
        if again in ["y", "n"]:
            if again == "y":
                print("Good choice!")
                return True
            else:
                print("See ya!")
                return False
        else:
            print("invalid choice")
        
def main():
    while True:
        attempts = 1
        num = random.randint(1, 100)
        print("Welcome to guessing a number between 1 and 100!")
        while True:
            guess_num = user_input()
            if check_num(guess_num, num, attempts):
                break
            else:
                attempts += 1
        if restart():
            None
        else:
            break

main()
            

    