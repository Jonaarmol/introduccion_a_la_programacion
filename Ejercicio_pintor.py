#Ejercicio n°2: 
'''
Un pintor de casas debe hacer un presupuesto para un cliente. Lo
que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El
cliente le indica que necesita conocer el costo de mano de obra para pintar una
pared rectangular de un galpón. El pintor cobra un monto fijo por cada metro
cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para
pintar la pared.
'''

#Código

wall_measurement = float(input('Ingrese la cantidad de m2 de la pared (sólo números): '));
price_per_m2 = float(input('Ingrese el precio de la mano de obra por m2 (sólo números): '));
bill = wall_measurement * price_per_m2
print(f'El precio de la mano de obra es: ${bill}')