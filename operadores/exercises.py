# Calculator
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicación:", num1 * num2)
if num2 != 0:
    print(f"División: {num1 / num2:.2f}\n")
    print(f"División baja: {num1 // num2}")
    print(f"Módulo: {num1 % num2}")
else:
    print("Error!\n")
print(f"Exponente: {num1 ** num2:.2f}\n")


# Even or odd
num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print("El número es par.\n")
else:
    print("El número es impar.\n")


# Time Converter
seconds = int(input("Ingrese el número de segundos: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60
hours = str(hours).zfill(2)
minutes = str(minutes).zfill(2)
seconds = str(remaining_seconds).zfill(2)
print(f"{hours}:{minutes}:{seconds}")


# Compare two numbers
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
print(num1 == num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)
print(num1 != num2)


#range check
age = int(input("\nIngrese su edad: "))
print(18 <= age <= 65)
print(age >= 18 and age <= 65)


discount = 0
price = float(input("\nIngrese el precio del producto: "))
quantity = int(input("Ingrese la cantidad de productos: "))
subtotal = price * quantity
if subtotal >= 100:
    print("El subtotal es mayor a 100. Se aplicará un descuento del 10%.")
    discount = subtotal * 0.1
total = subtotal - discount
tax = total * 0.18
print("Total a pagar:")
print(f"{total:.2f}")
print("Descuento aplicado:")
print(f"{discount:.2f}")
print("Subtotal:")
print(f"{subtotal:.2f}")
print("Impuesto aplicado: 18%")
print(f"{tax:.2f}")
print("Total a pagar con impuesto:")
print(f"{total + tax:.2f}")