'''
Un profesor de matemática necesita generar la tabla de multiplicar de un número entero comprendido entre 1 y 10. Por ejemplo para el 3 debería aparecer como salida:
3x1=3
3x2=6
3x3=9
…. y así hasta 10


Resuelva este problema utilizando un para

number = int(input("Ingrese el número del cual desea obtener la tabla de resultados: "));
print(f"La tabla del {number} es:")
for i in range(0, 11, 1):
    result = number * i
    print(f"{number}x{i}= {result}");

'''
#Resuelva este problema utilizando un mientras 

number = int(input("Ingrese el número del cual desea obtener la tabla de resultados: "));
counter = 0;

print(f"La tabla del {number} es:")

while counter <=10:
    result= counter * number
    print(f"{number}x{counter}= {result}");
    counter += 1