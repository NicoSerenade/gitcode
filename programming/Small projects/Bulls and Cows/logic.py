import random as r



def get_secret_number():
    numbers = [1,2,3,4,5,6,7,8,9,0]
    secret_number = r.sample(numbers, k=4)
    secret_number = "".join(map(str, secret_number))
    return secret_number

def get_bulls_and_cows(secret_number, guess):
    bulls_cows = {"BULLS":0, "COWS":0}

    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            bulls_cows["BULLS"] += 1
        elif guess[i] in secret_number:
            bulls_cows["COWS"] += 1

    return bulls_cows

def main(secret_number, guess):
    bulls_cows_result = get_bulls_and_cows(secret_number, guess)

    return bulls_cows_result["BULLS"], bulls_cows_result["COWS"]