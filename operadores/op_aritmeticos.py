suma = 12 + 5
resta = 12 - 5
multiplicacion = 12 * 5
division = 12 / 5   # devuelve un numero decimal (float)
division_baja = 12 // 5 # devuelve un numero entero (int) redondeado hacia abajo
modulo = 12 % 5 # devuelve el resto de la division, es decir, lo que sobra despues de dividir 12 entre 5. En este caso, el resultado es 2, porque 5 cabe en 12 dos veces (5 * 2 = 10) y sobra 2 para llegar a 12.
exponente = 12 ** 5 # devuelve 12 elevado a la potencia de 5


print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("División baja:", division_baja)
print("Módulo:", modulo)
print("Exponente:", exponente)

# tipo de dato
print(type(suma)) # int
print(type(division)) # float