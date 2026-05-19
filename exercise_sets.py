def clean_ingredients(nombre_plato, ingredientes):
    return (nombre_plato, set(ingredientes))

def check_drinks(nombre_bebida, ingredientes):

    ingredientes_set = set(ingredientes)
    
  
    if ingredientes_set.intersection(ALCOHOLS):
        return f"{nombre_bebida} Cocktail"
    else:
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
