es_igual_que = 5 == 5 # devuelve True porque ambos valores son iguales
print(es_igual_que)
es_igual_que = 5 == 3 # devuelve False porque ambos valores no son iguales  
print(es_igual_que)
es_mayor_que = 5 > 3 # devuelve True porque 5 es mayor que 3
print(es_mayor_que)
es_menor_que = 5 < 3 # devuelve False porque 5 no es menor que 3
print(es_menor_que)
es_mayor_o_igual_que = 5 >= 5 # devuelve True porque 5 es mayor o igual que 5
print(es_mayor_o_igual_que)
es_menor_o_igual_que = 5 <= 3 # devuelve False porque 5 no es menor o igual que 3
print(es_menor_o_igual_que)
es_diferente_que = 5 != 3 # devuelve True porque ambos valores son diferentes
print(es_diferente_que) 

# comparar cadenas de texto
contrasena_almacenada = "contraseña123"
contrasena_ingresada1 = "Contraseña123"
contrasena_ingresada2 = 'contraseña123'
contrasena_ingresada3 = """contraseña123"""

print("", contrasena_almacenada == contrasena_ingresada1) # devuelve False porque las mayúsculas y minúsculas son diferentes
print(contrasena_almacenada.lower() == contrasena_ingresada1.lower()) # devuelve True porque ambas contraseñas se convierten a minúsculas antes de compararlas
print(contrasena_almacenada == contrasena_ingresada2) # devuelve True porque ambas contraseñas son exactamente iguales, aun con el uso de comillas simples o dobles
print(contrasena_almacenada == contrasena_ingresada3) # devuelve True porque ambas contraseñas son exactamente iguales, aun con el uso de comillas triples