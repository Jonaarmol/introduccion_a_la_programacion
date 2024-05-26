Algoritmo despensa
		Definir cantidad_litros_leche  Como Entero
		Definir cliente_jubilado Como Entero
		Definir precio_por_litro, descuento_1, descuento_2, descuento_3, descuento_4, costo_total Como Real
		precio_por_litro = 1000
		Escribir "Ingrese la cantidad de litros de lleche que el cliente lleva:"
		Leer cantidad_litros_leche
		Escribir "¿El cliente es jubilado? 1. Si lo es. Cualquier otro número si no lo es"
		Leer cliente_jubilado
		descuento_1 = 0.90
		descuento_2 = 0.85
		descuento_3 = 0.80
		descuento_4 = 0.75
		
		Si cliente_jubilado = 1 Entonces
			Si cantidad_litros_leche > 12 Y cantidad_litros_leche <= 24 Entonces
				precio_total <- (cantidad_litros_leche * precio_por_litro) * descuento_3
			Sino
				Si cantidad_litros_leche > 24 Entonces
					precio_total <- (cantidad_litros_leche * precio_por_litro) * descuento_4
				Sino
					precio_total <- (cantidad_litros_leche * precio_por_litro) * descuento_1
				FinSi
			FinSi
		Sino
			Si cantidad_litros_leche > 12 Y cantidad_litros_leche <= 24 Entonces
				precio_total <- (cantidad_litros_leche * precio_por_litro) * descuento_1
			Sino
				Si cantidad_litros_leche > 24 Entonces
					precio_total <- (cantidad_litros_leche * precio_por_litro) * descuento_2
				Sino
					precio_total <- cantidad_litros_leche * precio_por_litro
				FinSi
			FinSi
		FinSi
		
		Escribir "El valor a pagar es: $", precio_total
FinAlgoritmo
