print("Hello, World!\n");

# This is a comment in Python. It is ignored by the interpreter.

# VALUES

'string'

"string"

"""
This is a multi-line string."""

'''
This is also a multi-line string.'''


40 # this is an integer

40.2 # this is a float

False # this is a boolean value

True # this is also a boolean value

# VARIABLES

x = 40 # this is an integer variable

a = 5
b = 8
c = a + b # this is an expression that adds a and b and assigns the result to c

print(x)

print(c)

# CONCATENATION

nombre = "Lucas"
bienvenida = "Hola, " + nombre + "! Como estas" # this is string concatenation
print(bienvenida)


# del nombre
# del is a keyword in Python that is used to delete a variable. After this line, the variable 'nombre' will no longer exist.
bienvenida2 = f"Hola, {nombre}! Como estas?" # this is string interpolation using f-strings
print(bienvenida2)

# search elements in string
# operator 'in' is used to check if a substring exists in a string. It returns True if the substring is found, otherwise it returns False.
print("ola" in bienvenida) # this will return True if 'ola' is in the string 'bienvenida'
print("ola" not in bienvenida2) # this will return False if 'ola' is in the string 'bienvenida2'


# camelCase
myVariableName = "This is a variable in camelCase"

# snake_case
my_variable_name = "This is a variable in snake_case" # snake_case is the most common convention for variable names in Python. It uses lowercase letters and underscores to separate words.

