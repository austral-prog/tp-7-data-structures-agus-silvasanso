def get_coordinate(registro):
    return registro[1]

def convert_coordinate(coordenada):
    return (coordenada[0], coordenada[1])

def create_record(registro_azara, registro_rui):
    coord_azara = get_coordinate(registro_azara)
    if convert_coordinate(coord_azara) == registro_rui[1]:
        # Al sumar dos tuplas, se concatenan en una sola
        return registro_azara + registro_rui
    return "not a match"

def sum_tuple(numeros):
    total = 0
    for num in numeros:
        total += num
    return total

def count_occurrences(tupla, elemento):
    contador = 0
    for item in tupla:
        if item == elemento:
            contador += 1
    return contador

def find_index(tupla, elemento):
    for i in range(len(tupla)):
        if tupla[i] == elemento:
            return i
    return -1

def filter_positives(numeros):
    positivos = []
    for num in numeros:
        if num > 0:
            positivos.append(num)
    # Convertimos la lista resultante de vuelta a tupla
    return tuple(positivos)
