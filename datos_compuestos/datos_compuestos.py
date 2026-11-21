# LIST
# son una manera de almacenar varios datos en una sola variable. 
# Pueden contener diferentes tipos de datos. 
# Basicamente una matriz de una sola fila, se pueden modificar, agregar o eliminar elementos.
lista = ["Lucas Dalto", "Soy Dalto", True, 1.85]
print(lista)

# Ejemplos
print(lista[0]) #Accedo al primer elemento de la lista
print(lista[1]) #Accedo al segundo elemento de la lista

# TUPLE
# son similares a las listas, pero no se pueden modificar una vez creadas. 
# Se utilizan para almacenar datos que no deben cambiar.
tupla = ("Lucas Dalto", "Soy Dalto", True, 1.85)
print(tupla)
print(tupla[0]) #Accedo al primer elemento de la tupla
print(tupla[3]) #Accedo al cuarto elemento de la tupla

# -------------------------------- IMPORTANTE --------------------------------
# para mostrar elementos tanto de tuplas como listas se usan corchetes [] 


# SET
# Son una colección de elementos únicos, se utilizan para almacenar datos que no deben repetirse.
# No permiten valores/datos duplicados y no mantienen un orden específico.
# Puede modificarse agregando o eliminando elementos, pero no se puede modificar un elemento existente. 
# Tampoco se puede acceder a los elementos de un conjunto por su índice, ya que no mantienen un orden específico, por lo tanto no pueden ser indexados (Ej.: "conjunto[0]").
conjunto = {"Lucas Dalto", "Soy Dalto", True, 1.85}
print(conjunto)


# DICTIONARY
# son una colección de pares clave-valor, donde cada clave es única. Se utilizan para almacenar datos que se pueden asociar con una clave específica.
# Es literalmente un JSON
# No se puede acceder a los elementos de un diccionario por su índice, ya que se accede a través de las claves.
diccionario = {"nombre": "Lucas Dalto",
"apellido": "Soy Dalto","es_programador": True,
"altura": 1.85}
print(diccionario)
print(diccionario["nombre"]) #Accedo al valor asociado a la clave "nombre" en el diccionario


