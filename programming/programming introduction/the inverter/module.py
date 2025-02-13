def take_last_digit(number: int)-> int:
    return number % 10

def quit_last_digit(number: int)-> int:
    return number // 10

def invert_number(number: int)-> int:
    number = number
    numbers = [] 
    for num in str(number):
        last_digit = take_last_digit(number)
        numbers.append(last_digit)
        number = quit_last_digit(number)
        int_number = "".join(map(str,numbers))
        
    return int(int_number)


