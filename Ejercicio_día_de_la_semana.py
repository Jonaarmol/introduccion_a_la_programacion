day = input("¿Qué día es hoy?");
first_char = day[0].upper()
left_chars = day[1:].lower()
converted_day =first_char+left_chars
days_of_week = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"] 
weekend_days = ["Sabado", "Domingo"]

while converted_day not in days_of_week and converted_day not in weekend_days:
    day = input("No ingresaste un día válido, ingrese nuevamente qué día es hoy: ")
    first_char = day[0].upper()
    left_chars = day[1:].lower()
    converted_day =first_char+left_chars
if converted_day in days_of_week:
    print("Ve a la escuela")
else:
    print("Que tengas un buen finde")
