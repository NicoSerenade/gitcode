import random
import sqlite3
import sys

MIN_DEPOSIT = 30
MIN_BET = 10

ROWS_COLS_LINES = 3
MAX_LINES = ROWS_COLS_LINES
ROWS = ROWS_COLS_LINES
COLS = ROWS_COLS_LINES

symbols = {'🐣': 3, '🦐': 9, '🐢': 27}
symbols_value = {'🐣': 100, '🦐': 10, '🐢': 2}

#SQLlite3 connection

def create_connection(): #This connect the database with python
    conn = sqlite3.connect('users.db') 
    return conn

def create_database(): 
    conn = create_connection()
    cursor = conn.cursor() # cursor allows to code in SQL language, and thus interact with and modify the database
    # SQL uses -- for coments
    # all inside the cursor.execute(''' ''') is SQL language
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS users ( -- users is the name of the table
        id INTEGER PRIMARY KEY AUTOINCREMENT, -- id is the first column and before the next comma its characteristics: INTEGER the type of variables PRIMARY KEY: makes the id column an unique identifier for each record AUTOINCREMENT: autoincrement the id for the next record. UNIQUE means the variables inside name cannot be repeated.
        name TEXT UNIQUE
    )
    ''')
    conn.commit() # saves the database changes 
    conn.close() # close the connection with the database

def check_name_database(name): 
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM users WHERE name = ?", (name,)) # Select a record from column name, in the users table, where that record be = ?. (name,) means the variable that I want to replace instead of ? 
    user = cursor.fetchone() # if a row matches with the user request, creates a tuple with that request ('nico',) else: None
    conn.close() # this close the connection with the database
    return user is not None # if user is None, returns False, else: True

def add_name_database(name):
    conn = create_connection()
    cursor = conn.cursor()
    try: # avoid that program stops if the except Error is found
        cursor.execute("INSERT INTO users (name) VALUES (?)", (name,)) # 1 INSERT INTO users: add a new row in users. 2 (name): means the column where the value will be recorded. 3 VALUES (?): announces that a value is going to de entered. 4 (name,): define the value. Note: I could do directly: VALUES ('{name}')" but is better not to insert values directly into SQL to avoid SQL injections.
    except sqlite3.IntegrityError: #error cause by a repeated name into the database
        print(f'{name} is already in the database.')

    conn.commit() 
    conn.close()

#Main loop

def main():
    while True:
        create_database()  # create table if it doesn't exist
        print_menu()
        name = user()
        is_registered = check_name_database(name)
        if is_registered:
            print(f'Welcome again {name.title()}.')
            balance = deposit()
            free_game = False
            wanna_quit = game(balance, free_game, name)

        elif not name:
            balance = deposit()
            free_game = False
            wanna_quit = game(balance, free_game, name)

        elif name and not is_registered:
            add_name_database(name)
            print(f'{name} has been registered successfully!')
            print(f'{name}, free spin has just started!')
            balance = 30
            free_game = True
            wanna_quit = game(balance, free_game, name)
            
        if wanna_quit:
            sys.exit()

        final_options()

def print_menu():
    print('-----Welcome to Nico\'s spin!-----')
    print('These are the multipliers')
    for icon, value in symbols_value.items():
        print(f'{icon} x {value}')

def user():
    while True:
        choice = input('Enter (y) for registration (and get a courtesy deposit of $30) or (n) for play as a guest: ') 
        if choice == 'n':
            name = None
            break
        elif choice == 'y':
            name = input('Please enter your name: ').title()
            break
        else:
            print('Invalid choice')
    return name

def game(balance, free_game, name):
    wanna_quit = False

    while balance >= MIN_DEPOSIT:
        print(f'Your current balance is ${balance}')
        spin = input('Enter (y) to spin, (n) to quit or (d) to deposit more money: ').lower()
        if spin == 'y':
            lines = get_lines_number()
            while True:
                bet = get_bet()
                total_bet = bet * lines
                if total_bet > balance:
                    print(f'You do not have enough money, your current balance is ${balance}')
                else:
                    break

            print(f'You are betting ${bet} in {lines} lines, for a total bet of ${total_bet}')
            columns = get_slot_machine_spin()
            print_slot_machine(columns)
            winnings, winning_lines, biggest_prize = check_winnings(columns, lines, bet, symbols_value)

            if biggest_prize:
                print(f'You spun the biggest prize {len(biggest_prize)} times!!!')

            if winnings:
                print(f'You won ${winnings}!')
                if len(winning_lines) > 1:
                    print(f'You won on line\'s: {", ".join(map(str, winning_lines))}') #If winning_lines = [1, 3, 5], after map(str, winning_lines), it becomes ['1', '3', '5']. 2) ", ".join(...) takes a list of strings and joins them together into a single string separated by what I put inside ' and '.join 
                else:
                    print(f'You won on line: {winning_lines[0]}')
            else:
                print('You have lost')

            profit = winnings - total_bet
            balance += profit
            free_game = False

        elif spin == 'n' and free_game:
            print("You can't quit on the first free spin!")

        elif spin == 'n':
            if name:
                print(f'Thank you for betting with us {name}, you left with ${balance}')
            else:
                print(f'Thank you for betting with us guest, you left with ${balance}')
            wanna_quit = True
            break

        elif spin == 'd':
            balance += deposit()

        else:
            print('Invalid choice')

    if spin != 'n':
        print(f'Your current balance is ${balance}')
        print(f'Minimum balance is ${MIN_DEPOSIT}')
        if name:
            print(f'Thank you for betting with us {name}, you left with ${balance}')
        else:
            print(f'Thank you for betting with us guest, you left with ${balance}')

    return wanna_quit

def deposit():
    while True:
        balance = input('How much would you like to deposit? $')
        if balance.isdigit():
            balance = int(balance)
            if balance >= MIN_DEPOSIT:
                break
            else:
                print(f'${MIN_DEPOSIT} is the minimum valid deposit.')
        else:
            print('Invalid value.')
    return balance

def get_lines_number():
    while True:
        print('If you bet on 1 line, means on line 1, betting on 2 lines, means on line 1 and 2, etc...')
        lines = input(f'Enter the number of lines to bet on. (1-{MAX_LINES}) ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f'it must be between (1-{MAX_LINES})')
        else:
            print('Invalid value.')
    return lines

def get_bet():
    while True:
        bet = input('How much would you like to bet on each line? $')
        if bet.isdigit():
            bet = int(bet)
            if bet >= MIN_BET:
                break
            else:
                print(f'${MIN_BET} is the minimum valid bet.')
        else:
            print('Invalid value.')
    return bet

def get_slot_machine_spin():
    all_symbols = []
    for symbol, symbol_number in symbols.items():
        for _ in range(symbol_number):
            all_symbols.append(symbol)

    columns = []
    for _ in range(COLS):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(ROWS):
            symbol = random.choice(current_symbols)
            current_symbols.remove(symbol)
            column.append(symbol)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i == len(columns) -1:
                print(column[row])
            else:
                print(column[row], end=' | ')

def check_winnings(columns, lines, bet, symbols_value):
    winnings = 0
    winning_lines = []
    biggest_prize = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol_check != symbol:
                break
        else: #Else in for loops only executes if the for loop do not breaks
            if symbol == '🐣':
                biggest_prize.append('🐣')
            winnings += symbols_value[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines, biggest_prize

def final_options():
    choice = input('Enter (y) for play again or (n) to exit the game: ').lower()
    while True:
        if choice == 'y':
            print('Great choice!\n')
            break
        elif choice == 'n':
            print('Until next time!\n')
            sys.exit()
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main() 