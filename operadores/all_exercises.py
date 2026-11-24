# leap year
userYear = int(input("Ingrese un año: "))
if(userYear%4 == 0 and userYear%100 != 0) or (userYear%400 == 0):
    print(f"{userYear} es un año bisiesto")
else:
    print(f"{userYear} no es un año bisiesto")

# Login check
userName = input("\n\nIngrese su nombre de usuario: ")
userPassword = input("Ingrese su contraseña: ")
if (userName == userPassword):
    print("Usuario y contraseña correctos")
else:
    print("Usuario o contraseña incorrectos")

# Triangle Validator
side1 = float(input("\nIngrese el primer lado del triángulo: "))
side2 = float(input("Ingrese el segundo lado del triángulo: "))
side3 = float(input("Ingrese el tercer lado del triángulo: "))
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    print("Los lados ingresados forman un triángulo")
    if (side1 == side2 == side3):
        print("El triángulo es equilátero")
    elif (side1 == side2) or (side1 == side3) or (side2 == side3):
        print("El triángulo es isósceles")
    else:
        print("El triángulo es escaleno")
else:
    print("Los lados ingresados no forman un triángulo")

# movie ticket price
base_ticket = 10.0
age = int(input("\nIngrese su edad: "))
if age < 12 or age >= 65:
    ticket_price = base_ticket * 0.5
    print(f"El precio del ticket es: ${ticket_price:.2f} (50% de descuento)")
else:
    student_status = input("¿Es estudiante? (s/n): ")
    if student_status.lower() == 's':
        ticket_price = base_ticket * 0.8
        print(f"El precio del ticket es: ${ticket_price:.2f} (20% de descuento)")
    else:
        print(f"El precio del ticket es: ${base_ticket:.2f} (precio completo)")

#number clasifier
number = int(input("\nIngrese un número: "))
if number > 0:
    print(f"{number} es un número positivo")
elif number < 0:
    print(f"{number} es un número negativo")
else:
    print(f"{number} es cero")
if number % 2 == 0:
    print(f"{number} es un número par")
else:
    print(f"{number} es un número impar")
if number % 5 == 0 and number % 3 == 0:
    print(f"{number} es divisible entre 5 y 3")
else:
    print(f"{number} no es divisible entre 5 y 3")
if len(str(number)) >= 2:
    if len(str(number)) == 2 and str(number)[0] != '-':
        print(f"{number} es un número de dos dígitos")
    elif len(str(number)) == 3:
        if str(number)[0] == '-':
            print(f"{number} es un número de dos dígitos negativo")
    else:
        print(f"{number} es un número de tres dígitos positivo")


# weekend planner
weekend = input("Es fin de semana? (s/n): ")
if weekend.lower() == 's':
    rain = input("¿Llueve? (s/n): ")
    if rain.lower() == 'n':
        dinero1 = input("¿Tienes mas de $50? (s/n): ")
        if dinero1.lower() == 's':
            print("Puedes ir a la playa")
        else:
            dinero2 = input("¿Tienes mas de $15? (s/n): ")
            if dinero2.lower() == 's':
                print("Puedes ir al cine")
            else:
                    print("Puedes quedarte en casa y ver una película")
    else:
        print("Puedes quedarte en casa y ver una película")
else:
    print("Ve a trabajar o a estudiar, es un día laborable")
