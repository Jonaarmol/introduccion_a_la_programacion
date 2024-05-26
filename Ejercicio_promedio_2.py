'''
En una escuela, luego de tomar un determinado examen, es necesario calcular el promedio de 
notas (las notas van de 0 a 10) de los alumnos de un curso. Se necesita saber si el 
rendimiento ha sido elevado (el promedio es mayor a 8), aceptable (el promedio está 
comprendido entre 6 y 8) o bajo (promedio es inferior a 6). 
Desarrollar un algoritmo que resuelva este problema. 
Para tener en cuenta: las autoridades del colegio saben cuántos estudiantes del curso 
han rendido el examen.

'''

students_quantity = int(input("Ingrese la cantidad de estudiantes que rindieron el examen: "));
total_grades = 0;

for i in range(students_quantity):
    grades = float(input("Ingrese la nota del alumno: "))
    total_grades += grades;

average = total_grades/students_quantity

if average >8:
    print(f"El promedio es de {average}, el rendimiento ha sido: elevado.")
elif average >= 6:
    print(f"El promedio es de {average}, el rendimiento ha sido: aceptable.")
else:
    print(f"El promedio es de {average}, el rendimiento ha sido: bajo.")






