#LIST: es un metodo que se utiliza para crear una lista a partir de un iterable, como una cadena o un rango. Devuelve una nueva lista con los elementos del iterable.
lista = list(["hola", "Lester", 34])

print(lista)

# LEN: es un metodo que se utiliza para obtener la longitud de una lista, es decir, el número de elementos que contiene. Devuelve un entero con la cantidad de elementos en la lista.
longitud = len(lista)
print(f"La longitud de la lista es: {longitud} elementos.")

# APPEND: es un metodo que se utiliza para agregar un elemento al final de una lista. Modifica la lista original y no devuelve ningún valor.
lista.append("Python")
print("Lista después de agregar un elemento:", lista)

# INSERT: es un metodo que se utiliza para insertar un elemento en una posición específica de una lista. Modifica la lista original y no devuelve ningún valor.
lista.insert(1, "programación")
print("Lista después de insertar un elemento en la posición 1:", lista)

# EXTEND: es un metodo que se utiliza para agregar los elementos de una lista a otra lista. Modifica la lista original y no devuelve ningún valor.
otra_lista = ["es", "genial"]
lista.extend(otra_lista)
print("Lista después de extender con otra lista:", lista)


# POP: es un metodo que se utiliza para eliminar y devolver el último elemento de una lista. Modifica la lista original y devuelve el elemento eliminado.
elemento_eliminado = lista.pop() # Si no existe un índice especificado (I.e.: lista.pop(1)), se elimina el último elemento de la lista.
# Si utilizamos un elemento negativo como índice (I.e.: lista.pop(-2)), se eliminará el elemento en la posición correspondiente contando desde el final de la lista (en este caso, el penúltimo elemento).
print(f"Elemento eliminado: {elemento_eliminado}")
print("Lista después de eliminar el último elemento:", lista)

# SORT: es un metodo que se utiliza para ordenar los elementos de una lista. Modifica la lista original y no devuelve ningún valor. Solo sirve para listas que contienen elementos del mismo tipo (I.e.: solo números o solo cadenas), ya que no se pueden comparar elementos de diferentes tipos.
numeros = [5, 2, 9, 1, 3]
numeros.sort()
print("Lista de números ordenada:", numeros)

# REVERSE: es un metodo que se utiliza para invertir el orden de los elementos de una lista. Modifica la lista original y no devuelve ningún valor.
numeros.reverse()
print("Lista de números invertida:", numeros)


# INDEX: es un metodo que se utiliza para obtener el índice de la primera aparición de un elemento en una lista. Devuelve un entero con el índice del elemento, o lanza una excepción si el elemento no se encuentra en la lista.
try:
    indice = lista.index("programación")
    print(f"El elemento 'programación' se encuentra en la lista en el índice {indice}.")
except ValueError:
    print("El elemento 'programación' no se encuentra en la lista.")

print(dir(lista)) # Muestra los métodos disponibles para el tipo de dato lista

# CLEAR: es un metodo que se utiliza para eliminar todos los elementos de una lista. Modifica la lista original y no devuelve ningún valor.
lista.clear()
print("Lista después de limpiar todos los elementos:", lista)