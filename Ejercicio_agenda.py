contact_list = {};
counter = 0;
flag = True;

while flag:
    user_selection = int(input("Seleccione una opción:\n1.Agregar persona.\n2.Modificar persona.\n3.Eliminar persona.\n4.Mostar agenda.\n5.Salir."))
    if user_selection == 1:
        last_name = input("Ingrese el apellido de esta persona: ")
        name = input("Ingrese el nombre de esta persona: ")
        dni = input("Ingrese el DNI de esta persona(sin puntos): ")
        email = input("Ingrese el e-mail de esta persona: ")
        phone_number = input("Ingrese el número de teléfono de esta persona: ")
        contact_list[counter] = {
            "Apellido": last_name,
            "Nombre": name,
            "dni": dni,
            "E-mail": email,
            "Número de teléfono": phone_number
            }
        counter += 1
        
    elif user_selection == 2:
        dni = int(input("Ingrese el DNI (sin puntos) de la persona que desea modificar:"))
        if dni in contact_list:
            if int(input("¿Desea modificar el apellido?: 1. Sí.\n2. No")) == 1:
                contact_list[dni]['Apellido'] = input("Ingrese el apellido: ")
            elif int(input("¿Desea modificar el nombre?: 1. Sí.\n2. No")) == 1:
                contact_list[dni]['Nombre'] = input("Ingrese el nombre: ")
            elif int(input("¿Desea modificar el DNI?: 1. Sí.\n2. No")) == 1:
                contact_list[dni]['DNI'] = input("Ingrese el DNI: ")
            elif int(input("¿Desea modificar el E-mail?: 1. Sí.\n2. No")) == 1:
                contact_list[dni]['E-mail'] = input("Ingrese el DNI: ")
            elif int(input("¿Desea modificar el Número de teléfono?: 1. Sí.\n2. No")) == 1:
                contact_list[dni]['Número de teléfono'] = input("Ingrese el número de teléfono: ")
        else:
            print("No existe el DNI en la agenda")
 
    elif user_selection == 3:
        dni = int(input("Ingrese el DNI (sin puntos) de la persona que desea eliminar:"))
        if dni in contact_list:
            del contact_list[dni]
        else:
            print("No existe el DNI en la agenda")
    
    elif user_selection == 4:
        print(contact_list)
    elif user_selection == 5:
        print("Ha salido con éxito, hasta luego!")
        flag = False
    else:
        input("Opción no válida, intente nuevamente.\n1.Agregar persona.\n2.Modificar persona.\n3.Eliminar persona.\n4.Mostar agenda.\n5.Salir.")








        


