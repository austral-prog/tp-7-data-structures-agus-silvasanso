def clean_ingredients(nombre_plato, ingredientes):
    # set() automáticamente elimina todos los duplicados
    return (nombre_plato, set(ingredientes))


def check_drinks(nombre_bebida, ingredientes):
    for ingrediente in ingredientes:
        if ingrediente in ALCOHOLS:
            return f"{nombre_bebida} Cocktail"
    return f"{nombre_bebida} Mocktail"


def unique_chars(texto):
    return set(texto)

def sum_set(numeros):
    total = 0
    for num in numeros:
        total += num
    return total

def common_elements(set_a, set_b):
    comunes = set()
    for elemento in set_a:
        if elemento in set_b:
            comunes.add(elemento)
    return comunes
