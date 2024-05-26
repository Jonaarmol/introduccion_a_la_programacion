Algoritmo puntos_torneo
	Definir partidos_ganados, partidos_empatados, partidos_perdidos Como Entero
	Definir sumatoria_final Como Real
	Escribir "Ingrese la cantidad de partidos ganados por el equipo: "
	Leer partidos_ganados
	Escribir "Ingrese la cantidad de partidos empatados por el equipo: "
	Leer partidos_empatados
	Escribir "Ingrese la cantidad de partidos perdidos por el equipo: "
	Leer partidos_perdidos
	sumatoria_final = (partidos_ganados*3)+partidos_empatados
	Escribir "El total de puntos del equipo es: " sumatoria_final
FinAlgoritmo
