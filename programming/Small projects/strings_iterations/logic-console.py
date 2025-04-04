
def encontrar_letra(string: str, char: str)-> int:
    index = -1
    iteration = 0
    while (iteration + 1) <= len(string) and index == -1:
        if char == string[iteration]:
            index = iteration
        iteration += 1

    return index

def contar(string: str, char: str)-> int:
    iteration = 0
    finds = 0
    while (iteration + 1) <= len(string):
        if char == string[iteration]:
            finds += 1
        iteration += 1
    return finds 

def letra_mas_repetida(string: str)-> str:
    if len(string) > 0:
        iteration = 0
        more_repeated = string[0]
        times_more_repeated = contar(string, string[0])

        while (iteration + 1) <= len(string):
            char_times = contar(string, string[iteration])
            if char_times > times_more_repeated:
                more_repeated = string[iteration]
                times_more_repeated = char_times
            iteration += 1
    else:
        more_repeated = ""
       
    return more_repeated

def encontrar_subcadena(string, substring):
    iteration = 0
    index = -1
    first_char = substring[0]
    while (iteration + 1) <= len(string) and index == -1:
        if first_char == string[iteration] and (len(string) - (iteration + 1)) >= len(substring):
            if string[iteration: (iteration + len(substring))] == substring:
                index = iteration
        iteration += 1

    return index

#console

string = "hola_mundo"
substring = "un"

print(encontrar_letra(string, substring))
print(contar(string, substring))
print(letra_mas_repetida(string))
print(encontrar_subcadena(string, substring))