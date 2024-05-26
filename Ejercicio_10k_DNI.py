items_quantity = int(input("Ingrese la cantidad de productos a pagar"));
total = 0;

for i in range(items_quantity):
    item_value = float(input("Ingrese el valor del producto"))
    total += item_value;

if total > 10000:
    print("El monto de su compra es mayor a $10.000, debe ingresar su DNI por razones de AFIP.")
    dni = input("Ingrese su DNI (sin puntos)")
    print(f'El monto total de la compra del cliente DNI: {dni}, es ${total}. Gracias por su compra!')
else:
    print(f'El total de la compra es ${total}. Gracias por su compra');

