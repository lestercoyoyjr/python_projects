print("Diferencia entre los diferentes cursos: ")
# en minutos y luego lo convertimos a horas
curso_actual = 90
curso_minimo = 150
curso_crudo1 = 210
curso_promedio = 240
curso_crudo2 = 300
curso_maximo = 420
print(f"Curso Actual: {curso_actual/60:.2f} horas")
print(f"Curso Mínimo: {curso_minimo/60:.2f} horas")
print(f"Curso Crudo 1: {curso_crudo1/60:.2f} horas")
print(f"Curso Promedio: {curso_promedio/60:.2f} horas")
print(f"Curso Crudo 2: {curso_crudo2/60:.2f} horas")
print(f"Curso Máximo: {curso_maximo/60:.2f} horas")

# Ejercicio A
diferencia_minimo = curso_minimo - curso_actual
print("Diferencia en horas entre el curso actual y:")
print(f"el curso mínimo: {diferencia_minimo/60:.2f} horas")
print(f"el curso máximo: {(curso_maximo - curso_actual)/60:.2f} horas")
print(f"El promedio entre todos los cursos es: {(curso_actual + curso_minimo + curso_crudo1 + curso_promedio + curso_crudo2 + curso_maximo)/6/60:.2f} horas")

# Ejercicio B
print("Porcentaje de material inservible que se reduce en: ")
print(f"El promedio de los cursos sin contar el curso actual: {(curso_crudo1 + curso_promedio + curso_crudo2 + curso_maximo)/4/60:.2f} horas")
print(f"El curso actual: {curso_actual/60:.2f} horas")

# Ejercicio C
print("Ver 10 horas de este curso es equivalente a ver: ")
print(f"El curso mínimo: {10/(curso_minimo/60):.2f} veces el curso mínimo")
print(f"El curso máximo: {10/(curso_maximo/60):.2f} veces el curso máximo")

