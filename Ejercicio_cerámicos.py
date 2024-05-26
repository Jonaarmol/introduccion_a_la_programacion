#Ejercicio n°4:
'''
Doña Rosa tiene un patio de forma rectangular y quiere cubrirlo con
cerámicos cuadrados. ¿Puedes ayudarla a calcular cuántos cerámicos necesitará?
'''
#Código

patio_length = float(input('Ingrese la cantidad de metros de ancho del patio: '));
patio_width = float(input('Ingrese la cantidad de metros de largo del patio: '));
tile_area_in_cm2 = float(input('Ingrese la cantidad de centímetros de largo o ancho de la baldosa: '))**2;
tile_area_in_m2 = tile_area_in_cm2/10000;
patio_area_in_m2 = patio_length*patio_width;
tile_quantity = patio_area_in_m2/tile_area_in_m2
print(f'La cantidad de baldosas necesarias son: {tile_quantity}')
