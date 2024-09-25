import random
import sys
import sqlite3

MIN_DEPOSIT = 30
MIN_BET = 10

COLS = 3
ROWS = 3
MAX_LINES = 3

SPECIAL_SYMBOL = '🐣'

symbols = {SPECIAL_SYMBOL: 3, '🦐': 9, '🐢': 27}
symbols_value = {SPECIAL_SYMBOL: 100, '🦐': 10, '🐢': 2}

#SQL

def create_conn():
    conn = sqlite3.connect('users.db')
    return conn

def create_database():
    conn = create_conn()
    c = conn.cursor()
    c.execute('''
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
                        )''')
    conn.commit()
    conn.close()

def check_name_database(name):
    conn = create_conn()
    c = conn.cursor()
    c.execute('SELECT name FROM users WHERE name = ?', (name,))
    user = c.fetchone()
    conn.close()
    return user is not None

def add_name_database(name):
    conn = create_conn()
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (name) VALUES (?)', (name,))
    except sqlite3.IntegrityError:
        print(f'{name} is already in the database')
    conn.commit()
    conn.close()

# main loop

def welcome():
    print('Welcome to The Big Turtle Spin Machine!')
    print('These are the multipliers:')
    for symbol, value in symbols_value.items():
        print(symbol, 'x', value)

def user():
    while True:
        choice = input("Enter (y) for sign in or registration (and get a free spin of $30), or (n) for play as a guest: " ).lower()
        if choice == 'y':
            name = input('Enter your name: ').title()
            break
        elif choice == 'n':
            name = None
            break
        else:
            print('Invalid choice')
    return name

def deposit():
    while True:
        balance = input(f'How much would you like to deposit? $')
        if balance.isdigit():
            balance = int(balance)
            if balance >= MIN_DEPOSIT:
                break
            else:
                print(f'{MIN_DEPOSIT} is the minimum valid deposit.')
        else:
            print('Invalid choice')
    return balance

def get_lines():
    while True:
        print('If you bet on 1 line, it will be on line 1, betting on 2 lines, on line 1 and 2, etc...')
        lines = input(f'Enter the number of lines to bet on. (1-{MAX_LINES}) ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f'it must be between (1-{MAX_LINES})')
        else:
            print('Invalid choice') 
    return lines

def get_bet(balance, lines):
    while True:
        bet = input(f'How much would you like to bet on each line? $')
        if bet.isdigit():
            bet = int(bet)
            if bet >= MIN_BET:
                total_bet = bet * lines
                if total_bet <= balance:
                    print(f"You're betting {bet} on {lines} lines, for a total bet of {total_bet}")
                    break
                else:
                    print(f"You have not enough money, your current balance is {balance}")
            else:
                print(f'{MIN_BET} is the minimum valid bet') #maybe I CODE IT TWICE        
        else:
            print('Invalid choice') 
    return bet, total_bet

def start_button():
    go_back = False
    while True:
        choice = input('Enter (y) to spin or (n) to change the bet: ')
        if choice == 'y':
            print('Good luck!')
            break
        elif choice == 'n':
            go_back = True
            break
        else:
            print('Invalid choice')
    return go_back

def create_spin():
    all_symbols = []
    for symbol, value in symbols.items():
        for _ in range(value):
            all_symbols.append(symbol)

    columns = []

    for _ in range(COLS):
        column = []
        current_symbols = all_symbols[:]

        for row in range(ROWS):
            symbol = random.choice(current_symbols)
            column.append(symbol)
            current_symbols.remove(symbol)
        columns.append(column)
    return columns

def print_spin(columns):
    for row in range(ROWS):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end= ' | ')
            else:
                print(column[row])

def check_spin(lines, columns, bet, symbols_value):
    winnings = 0
    winning_lines = []
    biggest_prize = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            check_symbol = column[line]
            if check_symbol != symbol:
                break
        else:
            if symbol == SPECIAL_SYMBOL:
                biggest_prize.append(symbol)
            winnings += symbols_value[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines, biggest_prize

def print_result(winnings, biggest_prize, winning_lines):
    if biggest_prize:
        print(f'Congratulations, you spun the biggest prize {len(biggest_prize)} TIMES! {SPECIAL_SYMBOL}')
    if winnings:
        print(f'You won ${winnings}!')
        if len(winning_lines) > 1:
            print(f"You won on lines {', '.join(map(str, winning_lines))}")
        else: 
            print('You won on line 1')
    else:
        print('You\'ve lost')

def game(name, balance, free_game):
    while True:
        while balance >= MIN_DEPOSIT:
            print(f'Your current balance is ${balance}')
            choice = input(f'Enter (y) to spin or (n) to quit: ')
            if choice == 'y':
                lines = get_lines()
                bet, total_bet = get_bet(balance, lines)
                while True:
                    go_back = start_button()
                    if go_back:
                        break
                    columns = create_spin()
                    print_spin(columns)
                    winnings, biggest_prize, winning_lines = check_spin(lines, columns, bet, symbols_value)
                    balance += winnings - total_bet
                    print_result(winnings, biggest_prize, winning_lines)
                    free_game = False
                    break

            elif choice == 'n' and free_game:
                print('You cannot quit in the first spin of free games')
            elif choice == 'n':
                if name:
                    print(f'Thank you for betting with us {name}, you left with ${balance}')
                else:
                    print(f'Thank you for betting with dear guest, you left with ${balance}')
                sys.exit()
            else: 
                print('Invalid choice')

        print(f'Your current balance is ${balance}')
        print(f'The minimum valid balance is ${MIN_DEPOSIT}')
        while True:
            choice = input(f'Enter (y) to deposit or (n) to quit')
            if choice == 'y':
                print('Great choice!')
                balance += deposit()
                break
            elif choice == 'n':
                if name:
                    print(f'Thank you for betting with us {name}, you left with ${balance}')
                else:
                    print(f'Thank you for betting with dear guest, you left with ${balance}')
                sys.exit()
            else:
                print('Invalid choice')
    
def main():
    create_database()
    free_game = False

    welcome()
    name = user()
    is_registered = check_name_database(name)
    if is_registered:
        print(f'Welcome again {name}!')
        balance = deposit()
        game(name, balance, free_game)

    elif name and not is_registered:
        print(f'{name} has been registered successfully')
        print(f'{name}, free spin has just started')
        balance = 30
        free_game = True
        game(name, balance, free_game)
    else:
        balance = deposit()
        game(name, balance, free_game)

if __name__ == '__main__':
    main()







