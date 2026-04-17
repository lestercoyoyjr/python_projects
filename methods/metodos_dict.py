diccionario = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "subs": 1000
}

# KEYS: devuelve una lista con las claves del diccionario. Tambien sirve para iterar sobre las claves del diccionario utilizando un bucle for.
claves = diccionario.keys()
print("Claves del diccionario:", claves)

# GET: devuelve el valor asociado a una clave especificada, o un valor predeterminado si la clave no se encuentra en el diccionario. Es una forma segura de acceder a los valores del diccionario sin lanzar una excepción si la clave no existe.
valor = diccionario.get("nombre")
print("Valor asociado a la clave 'nombre':", valor)
valor_no_existente = diccionario.get("edad", "Clave no encontrada")
print("Valor asociado a la clave 'edad':", valor_no_existente)

# ITEMS: devuelve una lista de tuplas, donde cada tupla contiene una clave y su valor asociado. Es útil para iterar sobre las claves y valores del diccionario utilizando un bucle for.
items = diccionario.items()
print("Claves y valores del diccionario:", items)


# POP: elimina una clave y su valor asociado del diccionario, y devuelve el valor eliminado. Modifica el diccionario original y devuelve el valor eliminado, o un valor predeterminado si la clave no se encuentra en el diccionario.
valor_eliminado = diccionario.pop("apellido", "Clave no encontrada")
print(f"Valor eliminado asociado a la clave 'apellido': {valor_eliminado}")
print("Diccionario después de eliminar la clave 'apellido':", diccionario)


# CLEAR: elimina todos los elementos del diccionario, dejando un diccionario vacío. Modifica el diccionario original y no devuelve ningún valor.
diccionario.clear()
print("Diccionario después de limpiar todos los elementos:", diccionario)