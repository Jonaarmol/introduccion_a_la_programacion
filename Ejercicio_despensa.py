'''
Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad. 
Si el cliente compra más de 12  unidades (y hasta 24 unidades), el costo tiene un descuento 
del 10%. Si compra más de 24 unidades, el descuento es del 15%. Además posee la promoción a 
los jubilados. La promoción de jubilados es sumarle un 10% de descuento 
(si posee otros descuentos, se suma los descuentos). 
Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.

'''
#Setting discounts, prices and retired possibilities 
discount_1 = 0.9;
discount_2 = 0.85;
discount_3 = 0.8;
discount_4 = 0.75;
price_per_litre = 1000;
retired_possibilities = [1, 2];

#Asking if the client is retired

is_retired = int(input("¿El cliente es jubilado?\nIngrese:\n 1 Si lo es. \n 2 Si no lo es."));

#If the input is not valid, ask to enter again the type of client 

while is_retired not in retired_possibilities:
   is_retired = int(input("No ingresó un número válido.\n¿El cliente es jubilado?\nIngrese:\n 1 Si lo es. \n 2 Si no lo es.")); 

#Asking how many litres of milk the client is buying

item_quantity = int(input("Cuántos litros de leche llevará el cliente?:"));

#Calculating the final price depending on the type of client and quantity of litres

if is_retired == 1:
    if item_quantity >12 and item_quantity <24:
        total = (item_quantity * price_per_litre)*discount_3
    elif item_quantity >24:
        total = (item_quantity * price_per_litre)*discount_4
    else:
        total = (item_quantity * price_per_litre)*discount_1
else: 
    if item_quantity >12 and item_quantity <24:
        total = (item_quantity * price_per_litre)*discount_1
    elif item_quantity >24:
        total = (item_quantity * price_per_litre)*discount_2
    else:
        total = (item_quantity * price_per_litre);

print(f"El valor a pagar es: ${total}");


   