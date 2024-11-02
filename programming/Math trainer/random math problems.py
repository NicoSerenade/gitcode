import random
import time

OPERATORS = '+', '-', '*', '/'
MIN_NUM = -9
MAX_NUM = 9
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_NUM, MAX_NUM)
    right = random.randint(MIN_NUM, MAX_NUM)
    operator = random.choice(OPERATORS)

    while operator == '/' and right == 0:
        right = random.randint(MIN_NUM, MAX_NUM)

    expr = str(left) + ' ' + operator + ' ' + str(right) # or: expr = f'{left} {operator} {right}'

    if operator == '/':
        answer = round(left / right) # rounds to the nearest even 

    else:
        answer = eval(expr)

    return expr, answer
input('Press enter to start ')
print('--------------------')

start_time = time.time()
wrong = 0
for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()

    while True:
        guess = input('Problem #' + str(i + 1) + '\n' + expr + ' = ') # or: guess = input(f'Problem #{i + 1}\n {expr} = ')
        if guess == str(answer):
            break
        wrong += 1
end_time = time.time()
total_time = end_time - start_time
print('--------------------')
print(f'Good job! You finished in {total_time:.2f}s with {wrong} answers wrong.') 


