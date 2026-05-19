def create_inventory(items):
    inventario = {}
    for item in items:
        if item in inventario:
            inventario[item] += 1
        else:
            inventario[item] = 1
    return inventario

def add_items(inventario, items):
    for item in items:
        if item in inventario:
            inventario[item] += 1
        else:
            inventario[item] = 1
    return inventario

def decrement_items(inventario, items):
    for item in items:
        if item in inventario and inventario[item] > 0:
            inventario[item] -= 1
    return inventario

def remove_item(inventario, item):
    if item in inventario:
        del inventario[item]
    return inventario

def list_inventory(inventario):
    resultado = []
    # .items() nos permite iterar la clave y el valor al mismo tiempo
    for item, cantidad in inventario.items():
        if cantidad > 0:
            resultado.append((item, cantidad))
    return resultado

def find_max_value(diccionario):
    if not diccionario:
        return ""
    
    max_nombre = ""
    max_puntaje = -float('inf') # Arrancamos con el número más bajo posible
    
    for nombre, puntaje in diccionario.items():
        if puntaje > max_puntaje:
            max_puntaje = puntaje
            max_nombre = nombre
    return max_nombre

def reverse_dict(diccionario):
    invertido = {}
    for clave, valor in diccionario.items():
        if valor in invertido:
            # Si el valor ya existe como clave nueva, le concatenamos el string
            invertido[valor] += clave
        else:
            invertido[valor] = clave
    return invertido

def word_frequency(palabras):
    # Manejo del caso borde explícito que pide la consigna
    if palabras == "":
        return {}
        
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

def find_biggest_expense(gastos):
    if not gastos:
        return ""
        
    max_categoria = ""
    max_promedio = -1
    
    for categoria, lista_gastos in gastos.items():
        if not lista_gastos:
            continue
        promedio = sum(lista_gastos) / len(lista_gastos)
        if promedio > max_promedio:
            max_promedio = promedio
            max_categoria = categoria
            
    return max_categoria

def sum_expenses(gastos):
    suma_total = {}
    for categoria, lista_gastos in gastos.items():
        suma_total[categoria] = sum(lista_gastos)
    return suma_total

def sum_expenses_by_type(gastos):
    suma_tipos = {}
    # Solo iteramos los valores, ya que no nos importa la categoría
    for lista_tuplas in gastos.values():
        for tipo, monto in lista_tuplas:
            if tipo in suma_tipos:
                suma_tipos[tipo] += monto
            else:
                suma_tipos[tipo] = monto
    return suma_tipos
