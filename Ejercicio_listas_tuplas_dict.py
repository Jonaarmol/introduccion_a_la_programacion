
#Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, 
#guardarlos en una lista y mostrarlos. 
'''
names = [];

while len(names) <10:
    name = input("Ingrese un nombre: ")
    first_char = name[0].upper()
    left_char= name[1:].lower()
    converted_name = first_char + left_char
    if converted_name not in names:
        names.append(converted_name)
    else:
        print("Nombre repetido, ingrese otro: ")
 
print(names)

#Eliminar la tercer y la última persona de la lista del ejercicio 1, 
#luego ordenar la lista y mostrarlo

names.pop(2)  
names.pop()
print(names)



#Guardar en un diccionario los datos de una persona: nombre, apellido, dni, email, 
#fecha de nacimiento.

dict_1 ={"Nombre": "Juan", "Apellido":  "Pérez" , "DNI": "11.111.111", "E-mail": "juanperez@gmail.com", "Fecha de nacimiento": "01/01/2000"};

print(dict_1)


#En un nuevo diccionario llamado familia guardar 4 personas, cada una de ellas con 
#los mismos 5 datos (nombre, apellido, dni, email, fecha de nacimiento)

familia = {{"Nombre": "Padre", "Apellido":  "Familia" , "DNI": "11.111.111", "E-mail": "padre@gmail.com", "Fecha de nacimiento": "01/01/2000"}, {"Nombre": "Madre", "Apellido":  "Familia" , "DNI": "22.222.222", "E-mail": "madre@gmail.com", "Fecha de nacimiento": "01/01/2000"}, {"Nombre": "Hija", "Apellido":  "Familia" , "DNI": "33.333.333", "E-mail": "hija@gmail.com", "Fecha de nacimiento": "01/06/2015"}, {"Nombre": "Hijo", "Apellido":  "Familia" , "DNI": "44.444.444", "E-mail": "hijo@gmail.com", "Fecha de nacimiento": "01/07/2015"}};

'''

#Guardar en una tupla los primeros n números pares. El valor de n que lo ingrese el 
#usuario (input). Luego mostrar los datos de la tupla.

n = int(input("Ingrese la cantidad de números pares que desea ver: "));
lista_numeros_pares = [];
contador = 0;

while len(lista_numeros_pares) <n:
    if contador % 2 == 0:
        lista_numeros_pares.append(contador)
    contador += 1;

tupla_numeros_pares = tuple(lista_numeros_pares);

print(tupla_numeros_pares);
print(len(tupla_numeros_pares));
print(type(tupla_numeros_pares));
    