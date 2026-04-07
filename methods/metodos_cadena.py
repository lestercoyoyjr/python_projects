cadena1 = "hola soy Dalto"
cadena2 = "Bienvenido maquinola"

# Métodos de cadenas
# DIR: muestra los métodos disponibles para un tipo de dato específico
print("Metodos disponibles para cadenas:")
print(dir(cadena1))
print("Metodos disponibles para enteros:")
print(dir(4)) # Muestra los métodos disponibles para el tipo de dato entero

# UPPER: convierte todos los caracteres de la cadena a mayúsculas
# LOWER: convierte todos los caracteres de la cadena a minúsculas
# CAPITALIZE: convierte el primer carácter de la cadena a mayúscula y el resto a minúsculas
print("Cadena original:", cadena1)
print("Cadena en mayúsculas:", cadena1.upper())
print("Cadena en minúsculas:", cadena1.lower())
print("Cadena con la primera letra en mayúscula:", cadena1.capitalize())

# FIND: busca una subcadena dentro de la cadena y devuelve el índice de la primera aparición, o -1 si no se encuentra
subcadena1 = "Dalto"
subcadena2 = "Python"
indice = cadena1.find(subcadena1)
if indice != -1:
    print(f"La subcadena '{subcadena1}' se encuentra en la cadena original en el índice {indice}.")
else:
    print(f"La subcadena '{subcadena1}' no se encuentra en la cadena original.")

indice = cadena1.find(subcadena2)
if indice != -1:
    print(f"La subcadena '{subcadena2}' se encuentra en la cadena original en el índice {indice}.")
else:
    print(f"La subcadena '{subcadena2}' no se encuentra en la cadena original.")

# INDEX: busca una subcadena dentro de la cadena y devuelve el índice de la primera aparición, o lanza una excepción si no se encuentra
try:
    indice = cadena1.index(subcadena1)
    print(f"La subcadena '{subcadena1}' se encuentra en la cadena original en el índice {indice}.")
except ValueError:
    print(f"La subcadena '{subcadena1}' no se encuentra en la cadena original.")

#ISNUMERIC: devuelve True si todos los caracteres de la cadena son dígitos, y False en caso contrario
cadena3 = "12345"
cadena4 = "12345abc"
print(f"¿La cadena '{cadena3}' es numérica?", cadena3.isnumeric())
print(f"¿La cadena '{cadena4}' es numérica?", cadena4.isnumeric())

# ISALPHA: devuelve True si todos los caracteres de la cadena son letras, y False en caso contrario
cadena5 = "HolaMundo"
cadena6 = "Hola Mundo"  
print(f"¿La cadena '{cadena5}' contiene solo letras?", cadena5.isalpha())
print(f"¿La cadena '{cadena6}' contiene solo letras?", cadena6.isalpha())