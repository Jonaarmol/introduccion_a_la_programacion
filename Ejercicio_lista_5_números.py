#Crear una lista de 5 números al azar (0 al 9) no repetidos y ordenados
import random

number_list_len = int(input("Ingrese la cantidad de números que quiere en su lista: "));
number_list = [];
number = random.randint(0, 9);

while len(number_list) < number_list_len:
    if number not in number_list:
        number_list.append(number);
    number = random.randint(0, 9);

number_list.sort();

print(number_list);
