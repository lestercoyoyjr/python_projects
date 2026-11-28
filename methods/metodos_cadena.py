# metodos de cadenas

cadena1 = "Hola maquinola soy Dalto"
cadena2 = "Bienvenido maquinola"
cadena3 = "12345"
cadena4 = 12345

print ("\n", dir(cadena1)) # muestra los métodos disponibles para un tipo de dato específico

resultado1 = cadena1.upper() # convierte todos los caracteres de la cadena a mayúsculas
print("\n", resultado1)

resultado2 = cadena1.lower() # convierte todos los caracteres de la cadena a minúsculas
print("\n", resultado2)


resultado3 = resultado2.capitalize() # convierte el primer carácter de la cadena a mayúscula y el resto a minúsculas
print("\n", resultado3)

busqueda_find = cadena1.find("a")
print("\n",busqueda_find) # busca una subcadena dentro de la cadena y devuelve el índice de la primera aparición, o -1 si no se encuentra

busqueda_index = cadena1.index("a")
print("\n",busqueda_index) # busca una subcadena dentro de la cadena y devuelve el índice de la primera aparición, o lanza una excepción si no se encuentra

# diferencia entre find e index: find devuelve -1 si no encuentra la subcadena, mientras que index lanza una excepción ValueError.

# isnumeric
 # devuelve True si todos los caracteres de la cadena son dígitos, y False en caso contrario
print("\n",cadena1.isnumeric())
print("\n",cadena3.isnumeric())
print("\n",str(cadena4).isnumeric()) # convierte el entero a cadena antes de llamar al método isnumeric, ya que es un método de cadenas y no de enteros.

# isalpha
cadena5 = "vjiosd"
print("\n",cadena1.isalpha())
print("\n",cadena3.isalpha())
print("\n",str(cadena5).isalpha()) # es true porque es alfanumerico

# count
contar_coincidencias = cadena1.count("a") # cuenta el número de veces que aparece una subcadena dentro de la cadena
print("\n",contar_coincidencias)
contar_caracteres = len(cadena1) # cuenta el número de caracteres de la cadena
print("\n",contar_caracteres)


# verificamos si una cadena empieza con una subcadena
empeiza_con = cadena1.startswith("Hola")
print("\n",empeiza_con)

# verificamos si una cadena termina con una subcadena
termina_con = cadena1.endswith("Dalto")
print("\n",termina_con)


# remplazar una subcadena por otra
reemplazar_texto = cadena1.replace("maquinola", "computadora")
print("\n",reemplazar_texto)

# separar la cadena
separar_texto = cadena1.split() # separa la cadena en una lista de subcadenas
print("\n",separar_texto)
separar_texto = cadena1.split("soy") # separa la cadena en una lista de subcadenas por el caracter especificado
print("\n",separar_texto)
print("\n",type(separar_texto)) # es una lista
