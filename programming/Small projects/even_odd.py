




def even_odd(num):
    if num % 2 == 1:
        return "is odd"
    else:
        return "is even"


def ask_for():
    while True:
        choice = input("do you wanna check another num? (y/n): ")
        if choice in ["y", "n"]:
            if choice == "y":
                return True
            else:
                return False
        else:
            print("invalid choice")

def main():
    while True:
        num = int(input("Please enter a number: "))
        print(even_odd(num))
        if not ask_for():
            print("Good bye!") 
            break
        
        else:
            None
            
main()