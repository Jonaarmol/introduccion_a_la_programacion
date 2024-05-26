import pandas as pd

# opción 1: le pido al usuario que ingrese la cantidad de notas que quiere ingresar:
'''
divisor = int(input("Ingresá la cantidad de notas para calcular el promedio: "));
suma_notas = 0;

for i in range(divisor):
  nota= float(input("Ingresá la nota: "))
  suma_notas += nota

promedio = suma_notas/divisor;

print(f'El promedio es {promedio}')
'''

# opción 2: le pido al usuario que ingrese directamente las notas:
'''
suma_notas_2 = 0;
contador = 0;

notas_2 = input("Ingresá tu nota o 'Enter' para salir")

while notas_2 !='':
  nota_3 = float(notas_2)   
  suma_notas_2 += nota_3
  contador +=1
  print(f'suma_notas vale {suma_notas_2}')
  print(f'contador vale {contador}')
  notas_2 = input("Ingresá tu nota o 'Enter' para salir");

promedio_2= suma_notas_2/contador
print(f'Tu promedio es: {promedio_2}');

'''

# opción 3: con array
'''
lista_notas = [];
suma_notas_3 = 0;
notas_3 = input("Ingresá tu nota o 'Enter' para salir");

while notas_3 != '':
    nota_4 = float(notas_3);
    lista_notas.append(nota_4);
    suma_notas_3+= nota_4;
    print (f'La lista de notas es {lista_notas} y la suma de notas es {suma_notas_3}');
    notas_3 = input("Ingresá tu nota o 'Enter' para salir");

divisor = len(lista_notas)

promedio_3 = suma_notas_3/divisor

print(f'El promedio es: {promedio_3}')

'''






