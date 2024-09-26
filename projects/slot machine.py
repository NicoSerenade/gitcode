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

countries_code = {
    'ANDORRA': 'AD', 'UNITED ARAB EMIRATES': 'AE', 'AFGHANISTAN': 'AF', 'ANTIGUA AND BARBUDA': 'AG', 'ANGUILLA': 'AI', 'ALBANIA': 'AL', 'ARMENIA': 'AM', 'NETHERLANDS ANTILLES': 'AN', 'ANGOLA': 'AO', 'ANTARCTICA': 'AQ', 'ARGENTINA': 'AR', 'AMERICAN SAMOA': 'AS', 'AUSTRIA': 'AT', 'AUSTRALIA': 'AU', 'ARUBA': 'AW', 'ALAND ISLANDS': 'AX', 'AZERBAIJAN': 'AZ', 'BOSNIA AND HERZEGOVINA': 'BA', 'BARBADOS': 'BB', 'BANGLADESH': 'BD', 'BELGIUM': 'BE', 'BURKINA FASO': 'BF', 'BULGARIA': 'BG', 'BAHRAIN': 'BH', 'BURUNDI': 'BI', 'BENIN': 'BJ', 'SAINT BARTHELEMY': 'BL', 'BERMUDA': 'BM', 'BRUNEI DARUSSALAM': 'BN', 'BOLIVIA, PLURINATIONAL STATE OF': 'BO', 'BONAIRE, SAINT EUSTATIUS AND SABA': 'BQ', 'BRAZIL': 'BR', 'BAHAMAS': 'BS', 'BHUTAN': 'BT', 'BOUVET ISLAND': 'BV', 'BOTSWANA': 'BW', 'BELARUS': 'BY', 'BELIZE': 'BZ', 'CANADA': 'CA', 'COCOS (KEELING) ISLANDS': 'CC', 'CONGO, THE DEMOCRATIC REPUBLIC OF THE': 'CD', 'CENTRAL AFRICAN REPUBLIC': 'CF', 'CONGO': 'CG', 'SWITZERLAND': 'CH', "COTE D'IVOIRE": 'CI', 'COOK ISLANDS': 'CK', 'CHILE': 'CL', 'CAMEROON': 'CM', 'CHINA': 'CN', 'COLOMBIA': 'CO', 'COSTA RICA': 'CR', 'CUBA': 'CU', 'CAPE VERDE': 'CV', 'CURACAO': 'CW', 'CHRISTMAS ISLAND': 'CX', 'CYPRUS': 'CY', 'CZECH REPUBLIC': 'CZ', 'GERMANY': 'DE', 'DJIBOUTI': 'DJ', 'DENMARK': 'DK', 'DOMINICA': 'DM', 'DOMINICAN REPUBLIC': 'DO', 'ALGERIA': 'DZ', 'ECUADOR': 'EC', 'ESTONIA': 'EE', 'EGYPT': 'EG', 'WESTERN SAHARA': 'EH', 'ERITREA': 'ER', 'SPAIN': 'ES', 'ETHIOPIA': 'ET', 'FINLAND': 'FI', 'FIJI': 'FJ', 'FALKLAND ISLANDS (MALVINAS)': 'FK', 'MICRONESIA, FEDERATED STATES OF': 'FM', 'FAROE ISLANDS': 'FO', 'FRANCE': 'FR', 'GABON': 'GA', 'UNITED KINGDOM': 'GB', 'GRENADA': 'GD', 'GEORGIA': 'GE', 'FRENCH GUIANA': 'GF', 'GUERNSEY': 'GG', 'GHANA': 'GH', 'GIBRALTAR': 'GI', 'GREENLAND': 'GL', 'GAMBIA': 'GM', 'GUINEA': 'GN', 'GUADELOUPE': 'GP', 'EQUATORIAL GUINEA': 'GQ', 'GREECE': 'GR', 'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS': 'GS', 'GUATEMALA': 'GT', 'GUAM': 'GU', 'GUINEA-BISSAU': 'GW', 'GUYANA': 'GY', 'HONG KONG': 'HK', 'HEARD ISLAND AND MCDONALD ISLANDS': 'HM', 'HONDURAS': 'HN', 'CROATIA': 'HR', 'HAITI': 'HT', 'HUNGARY': 'HU', 'INDONESIA': 'ID', 'IRELAND': 'IE', 'ISRAEL': 'IL', 'ISLE OF MAN': 'IM', 'INDIA': 'IN', 'BRITISH INDIAN OCEAN TERRITORY': 'IO', 'IRAQ': 'IQ', 'IRAN, ISLAMIC REPUBLIC OF': 'IR', 'ICELAND': 'IS', 'ITALY': 'IT', 'JERSEY': 'JE', 'JAMAICA': 'JM', 'JORDAN': 'JO', 'JAPAN': 'JP', 'KENYA': 'KE', 'KYRGYZSTAN': 'KG', 'CAMBODIA': 'KH', 'KIRIBATI': 'KI', 'COMOROS': 'KM', 'SAINT KITTS AND NEVIS': 'KN', "KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF": 'KP', 'KOREA, REPUBLIC OF': 'KR', 'KUWAIT': 'KW', 'CAYMAN ISLANDS': 'KY', 'KAZAKHSTAN': 'KZ', "LAO PEOPLE'S DEMOCRATIC REPUBLIC": 'LA', 'LEBANON': 'LB', 'SAINT LUCIA': 'LC', 'LIECHTENSTEIN': 'LI', 'SRI LANKA': 'LK', 'LIBERIA': 'LR', 'LESOTHO': 'LS', 'LITHUANIA': 'LT', 'LUXEMBOURG': 'LU', 'LATVIA': 'LV', 'LIBYAN ARAB JAMAHIRIYA': 'LY', 'MOROCCO': 'MA', 'MONACO': 'MC', 'MOLDOVA, REPUBLIC OF': 'MD', 'MONTENEGRO': 'ME', 'SAINT MARTIN (FRENCH PART)': 'MF', 'MADAGASCAR': 'MG', 'MARSHALL ISLANDS': 'MH', 'MACEDONIA, REPUBLIC OF': 'MK', 'MALI': 'ML', 'MYANMAR': 'MM', 'MONGOLIA': 'MN', 'MACAO': 'MO', 'NORTHERN MARIANA ISLANDS': 'MP', 'MARTINIQUE': 'MQ', 'MAURITANIA': 'MR', 'MONTSERRAT': 'MS', 'MALTA': 'MT', 'MAURITIUS': 'MU', 'MALDIVES': 'MV', 'MALAWI': 'MW', 'MEXICO': 'MX', 'MALAYSIA': 'MY', 'MOZAMBIQUE': 'MZ', 'NAMIBIA': 'NA', 'NEW CALEDONIA': 'NC', 'NIGER': 'NE', 'NORFOLK ISLAND': 'NF', 'NIGERIA': 'NG', 'NICARAGUA': 'NI', 'NETHERLANDS': 'NL', 'NORWAY': 'NO', 'NEPAL': 'NP', 'NAURU': 'NR', 'NIUE': 'NU', 'NEW ZEALAND': 'NZ', 'OMAN': 'OM', 'PANAMA': 'PA', 'PERU': 'PE', 'FRENCH POLYNESIA': 'PF', 'PAPUA NEW GUINEA': 'PG', 'PHILIPPINES': 'PH', 'PAKISTAN': 'PK', 'POLAND': 'PL', 'SAINT PIERRE AND MIQUELON': 'PM', 'PITCAIRN': 'PN', 'PUERTO RICO': 'PR', 'PALESTINIAN TERRITORY, OCCUPIED': 'PS', 'PORTUGAL': 'PT', 'PALAU': 'PW', 'PARAGUAY': 'PY', 'QATAR': 'QA', 'REUNION': 'RE', 'ROMANIA': 'RO', 'SERBIA': 'RS', 'RUSSIAN FEDERATION': 'RU', 'RWANDA': 'RW', 'SAUDI ARABIA': 'SA', 'SOLOMON ISLANDS': 'SB', 'SEYCHELLES': 'SC', 'SUDAN': 'SD', 'SWEDEN': 'SE', 'SINGAPORE': 'SG', 'SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA': 'SH', 'SLOVENIA': 'SI', 'SVALBARD AND JAN MAYEN': 'SJ', 'SLOVAKIA': 'SK', 'SIERRA LEONE': 'SL', 'SAN MARINO': 'SM', 'SENEGAL': 'SN', 'SOMALIA': 'SO', 'SURINAME': 'SR', 'SAO TOME AND PRINCIPE': 'ST', 'EL SALVADOR': 'SV', 'SINT MAARTEN': 'SX', 'SYRIAN ARAB REPUBLIC': 'SY', 'SWAZILAND': 'SZ', 'TURKS AND CAICOS ISLANDS': 'TC', 'CHAD': 'TD', 'FRENCH SOUTHERN TERRITORIES': 'TF', 'TOGO': 'TG', 'THAILAND': 'TH', 'TAJIKISTAN': 'TJ', 'TOKELAU': 'TK', 'TIMOR-LESTE': 'TL', 'TURKMENISTAN': 'TM', 'TUNISIA': 'TN', 'TONGA': 'TO', 'TURKEY': 'TR', 'TRINIDAD AND TOBAGO': 'TT', 'TUVALU': 'TV', 'TAIWAN, PROVINCE OF CHINA': 'TW', 'TANZANIA, UNITED REPUBLIC OF': 'TZ', 'UKRAINE': 'UA', 'UGANDA': 'UG', 'UNITED STATES MINOR OUTLYING ISLANDS': 'UM', 'UNITED STATES': 'US', 'URUGUAY': 'UY', 'UZBEKISTAN': 'UZ', 'HOLY SEE (VATICAN CITY STATE)': 'VA', 'SAINT VINCENT AND THE GRENADINES': 'VC', 'VENEZUELA, BOLIVARIAN REPUBLIC OF': 'VE', 'VIRGIN ISLANDS, BRITISH': 'VG', 'VIRGIN ISLANDS, U.S.': 'VI', 'VIET NAM': 'VN', 'VANUATU': 'VU', 'WALLIS AND FUTUNA': 'WF', 'SAMOA': 'WS', 'YEMEN': 'YE', 'MAYOTTE': 'YT', 'SOUTH AFRICA': 'ZA', 'ZAMBIA': 'ZM', 'ZIMBABWE': 'ZW'}

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
        name TEXT UNIQUE,
        streak INTEGER,
        flag TEXT)
            ''')
    conn.commit()
    conn.close()

def check_name_database(name):
    conn = create_conn()
    c = conn.cursor()
    c.execute('SELECT name FROM users WHERE name = ?', (name,))
    user = c.fetchone()
    conn.close()
    return user is not None

def add_user_database(name, flag):
    conn = create_conn()
    c = conn.cursor()
    c.execute('INSERT INTO users (name, flag) VALUES (?, ?)', (name, flag))
    conn.commit()
    conn.close()

def check_database_streak(name):
    conn = create_conn()
    c = conn.cursor()
    c.execute('SELECT streak FROM users WHERE name = ?', (name,))
    database_streak = c.fetchone() #creates a tuple with the columns results I asked for a specific row (THE TUPLE IS THE ROW)
    conn.close()
    if database_streak[0] is not None: #IF FIRST VALUE OF THE TUPLE is not None:
        return database_streak[0]
    else:
        return 0

def add_winning_streak(max_streak, name, database_streak):
    if max_streak >= database_streak:
        conn = create_conn()
        c = conn.cursor()
        c.execute('UPDATE users SET streak = ? WHERE name = ?',(max_streak, name))
        conn.commit()
        conn.close()

def print_hall_of_fame():
    conn = create_conn()
    c = conn.cursor()
    c.execute('''
        SELECT name, streak, flag
        FROM users
        ORDER BY streak DESC
        LIMIT 5
            ''')
    hall_of_fame = c.fetchall() # [(name, streak), (name, streak)]
    if hall_of_fame:
        print('Hall of Fame - Top 5 Streaks')
        for i, (name, streak, flag)  in enumerate(hall_of_fame):
            print(f'Rank: {i + 1}. {name}, max streak: {streak}. {flag}')

#main loop

def welcome():
    print('Welcome to The Big Turtle Spin Machine!')
    print('These are the multipliers:')
    for symbol, value in symbols_value.items():
        print(symbol, 'x', value)

def user():
    while True:
        choice = input("Enter (y) for sign in or registration (and get a free spin of $30), or (n) for play as a guest: " ).lower()
        if choice == 'y':
            full_name = input('Enter your name: ').title()
            name = full_name.split()[0]
            while True:
                country = input('Enter your country: ').upper()
                if country in countries_code:
                    flag = countries_code.get(country, '')
                    break
                else:
                    print('Invalid country')
                    print('Example: United States')
            break
        elif choice == 'n':
            name = None
            flag = None
            break
        else:
            print('Invalid choice')
    return name, flag

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
        lines = input(f'Enter the number of lines to bet on (1-{MAX_LINES}): ')
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
                    print(f"You're betting ${bet} on {lines} lines, for a total bet of ${total_bet}")
                    break
                else:
                    print(f"You have not enough money, your current balance is ${balance}")
            else:
                print(f'{MIN_BET} is the minimum valid bet')     
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
    biggest_prize = 0
    
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            check_symbol = column[line]
            if check_symbol != symbol:
                break
        else:
            winnings += symbols_value[symbol] * bet
            winning_lines.append(line + 1)
            if symbol == SPECIAL_SYMBOL:
                biggest_prize += 1

    return winnings, winning_lines, biggest_prize

def check_streak(winnings):
    if winnings:
        streak = 1
    else:
        streak = 0
    return streak

def print_result(winnings, biggest_prize, winning_lines):
    if biggest_prize > 0:
        print(f'Congratulations, you spun the biggest prize {biggest_prize} TIMES! {SPECIAL_SYMBOL}')
    if winnings > 0:
        print(f'You won ${winnings}!')
        if len(winning_lines) > 1:
            print(f"You won on lines {', '.join(map(str, winning_lines))}")
        else: 
            print('You won on line 1')
    else:
        print('You\'ve lost')

def game(name, balance, free_game, database_streak):
    all_winning_streak = []
    winning_streak = 0
    max_streak = 0

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
                    winnings, winning_lines, biggest_prize = check_spin(lines, columns, bet, symbols_value)
                    balance += winnings - total_bet
                    if not winnings:
                        winning_streak = 0
                    winning_streak += check_streak(winnings)
                    all_winning_streak.append(winning_streak)
                    max_streak = max(all_winning_streak)
                    print_result(winnings, biggest_prize, winning_lines)
                    free_game = False
                    break

            elif choice == 'n' and free_game:
                print('You cannot quit in the first spin of free games')
            elif choice == 'n':
                if name:
                    print(f'Thank you for betting with us {name}, you left with ${balance}')
                    print(f'You\'ve got a maximum streak of {max_streak} winnings')
                    add_winning_streak(max_streak, name, database_streak)
                else:
                    print(f'Thank you for betting with dear guest, you left with ${balance}')
                sys.exit()
            else: 
                print('Invalid choice')

        print(f'Your current balance is ${balance}')
        print(f'The minimum valid balance is ${MIN_DEPOSIT}')
        while True:
            choice = input(f'Enter (y) to deposit or (n) to quit: ')
            if choice == 'y':
                print('Great choice!')
                balance += deposit()
                break
            elif choice == 'n':
                if name:
                    print(f'Thank you for betting with us {name}, you left with ${balance}')
                    print(f'You\'ve got a maximum streak of {max_streak} winnings')
                    add_winning_streak(max_streak, name, database_streak)
                else:
                    print(f'Thank you for betting with dear guest, you left with ${balance}')
                sys.exit()
            else:
                print('Invalid choice')
    
def main():
    create_database()
    free_game = False

    print_hall_of_fame()
    welcome()
    name, flag = user()
    is_registered = check_name_database(name)
    if is_registered:
        database_streak = check_database_streak(name)
        print(f'Welcome again {name}!')
        balance = deposit()
        game(name, balance, free_game, database_streak)

    elif name and not is_registered:
        print(f'{name} has been registered successfully')
        print(f'{name}, free spin has just started')
        add_user_database(name, flag)
        database_streak = check_database_streak(name)
        balance = 30
        free_game = True
        game(name, balance, free_game, database_streak)
    else:
        balance = deposit()
        game(name, balance, free_game, database_streak)

if __name__ == '__main__':
    main()




