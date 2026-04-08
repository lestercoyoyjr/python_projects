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

# COUNT: cuenta el número de veces que una subcadena aparece en la cadena original
subcadena3 = "o"
conteo = cadena1.count(subcadena3)
print(f"La subcadena '{subcadena3}' aparece {conteo} veces en la cadena original.")

# LEN: devuelve la longitud de la cadena, es decir, el número de caracteres que contiene
longitud = len(cadena1)
print(f"La longitud de la cadena original es: {longitud} caracteres.")

# STARTSWITH: devuelve True si la cadena original comienza con la subcadena especificada, y False en caso contrario
subcadena4 = "hola"
subcadena5 = "Hola"
print(f"¿La cadena original comienza con '{subcadena4}'?", cadena1.startswith(subcadena4))
print(f"¿La cadena original comienza con '{subcadena5}'?", cadena1.startswith(subcadena5))

# ENDSWITH: devuelve True si la cadena original termina con la subcadena especificada, y False en caso contrario
subcadena6 = "Dalto"
subcadena7 = "dalto"
print(f"¿La cadena original termina con '{subcadena6}'?", cadena1.endswith(subcadena6))
print(f"¿La cadena original termina con '{subcadena7}'?", cadena1.endswith(subcadena7))

# REPLACE: reemplaza todas las apariciones de una subcadena por otra subcadena especificada
subcadena8 = "Dalto"
nueva_subcadena = "Python"
cadena_modificada = cadena1.replace(subcadena8, nueva_subcadena)
print("Cadena original:", cadena1)
print("Cadena modificada:", cadena_modificada)

# SPLIT: divide la cadena en una lista de subcadenas utilizando un separador especificado (por defecto es el espacio)
separador = " "
subcadenas = cadena1.split(separador)
print("Cadena original:", cadena1)
print("Subcadenas:", subcadenas)