

# Json de información de estudiantes

estudiantes = [
    {
        'Nombre': 'Luis', 'Apellido': 'Cedillo', 'Edad': '19', 'Grado': '6to', 'Grupo': 'CCH - B', 'Promedio': 8.2, 'Número de lista': '3'
    },
    {
        'Nombre': 'Aitana', 'Apellido': 'Luaces', 'Edad': '18', 'Grado': '6to', 'Grupo': 'CCH - B', 'Promedio': 6.7, 'Número de lista': '3'
    },
    {
        'Nombre': 'Alejandra', 'Apellido': 'Azuela', 'Edad': '18', 'Grado': '6to', 'Grupo': 'CCH - B', 'Promedio': 1, 'Número de lista': '1'
    },
    {
        'Nombre': 'Fernanda', 'Apellido': 'Coldado', 'Edad': '18', 'Grado': '6to', 'Grupo': 'CCH - B', 'Promedio': 7.8, 'Número de lista': '2'

    },
    {
        'Nombre': 'Valeria Alejandra', 'Apellido': 'Carrillo', 'Edad': '17', 'Grado': '6to', 'Grupo': 'CCH - B', 'Promedio': 4.3, 'Número de lista': '3'
    },
    {
        'Nombre': 'Alexandra', 'Apellido': 'El-Khalili', 'Edad': '18', 'Grado': '6to', 'Grupo': 'CCH - B', 'Promedio': 2.1, 'Número de lista': '3'
    },
    {
        'Nombre': 'Ligia', 'Apellido': 'Cortes', 'Edad': '18', 'Grado': '6to', 'Grupo': 'CCH - B', 'Promedio': 3.65, 'Número de lista': '3'
    },
    {
        'Nombre': 'Derek', 'Apellido': 'Emilio', 'Edad': '17', 'Grado': '6to', 'Grupo': 'CCH - B', 'Promedio': 7.2, 'Número de lista': '3'
    },
    {
        'Nombre': 'Juan', 'Apellido': 'Gonzalez', 'Edad': '18', 'Grado': '6to', 'Grupo': 'CCH - B', 'Promedio': 9, 'Número de lista': '3'
    },
]


def acomodar_list(estudiantes):
    """
    Funcion que acomoda la lista de estudiantes en función al filtro que se le pase
    """

    filter_by = str(input("Elige el filtro que quieres utilizar: "))

    if filter_by:
        option = int(
            input("1. Ordenar de menor a mayor\n2. Ordenar de mayor a menor\nIngrese una opcion: "))

        if isinstance(filter_by, int) and filter_by == 'Promedio':
            if option and option != 0:
                if isinstance(option, int) and option == 1:
                    for student in range(len(estudiantes)):
                        for value in range(student + 1, len(estudiantes)):
                            if estudiantes[student]['Promedio'] > estudiantes[value]['Promedio']:
                                estudiantes[student], estudiantes[value] = estudiantes[value], estudiantes[student]

                elif isinstance(option, int) and option == 2:
                    for student in range(len(estudiantes)):
                        for value in range(student + 1, len(estudiantes)):
                            if estudiantes[student]['Promedio'] < estudiantes[value]['Promedio']:
                                estudiantes[student], estudiantes[value] = estudiantes[value], estudiantes[student]
                else:
                    print("No se ha ingresado una opcion valida")
            else:
                print("No se ha ingresado información para opción")

        elif isinstance(filter_by, str) and filter_by == 'Edad':
            if option and option != 0:
                if isinstance(option, int) and option == 1:
                    for student in range(len(estudiantes)):
                        for value in range(student + 1, len(estudiantes)):
                            if estudiantes[student]['Edad'] > estudiantes[value]['Edad']:
                                estudiantes[student], estudiantes[value] = estudiantes[value], estudiantes[student]

                elif isinstance(option, int) and option == 2:
                    for student in range(len(estudiantes)):
                        for value in range(student + 1, len(estudiantes)):
                            if estudiantes[student]['Edad'] < estudiantes[value]['Edad']:
                                estudiantes[student], estudiantes[value] = estudiantes[value], estudiantes[student]
            else:
                print("No se ha ingresado una opcion valida")

        elif isinstance(filter_by, str) and filter_by == 'Nombre':
            if option and option != 0:
                if isinstance(option, int) and option == 1:
                    for student in range(len(estudiantes)):
                        for value in range(student + 1, len(estudiantes)):
                            if estudiantes[student]['Nombre'] > estudiantes[value]['Nombre']:
                                estudiantes[student], estudiantes[value] = estudiantes[value], estudiantes[student]

                elif isinstance(option, int) and option == 2:
                    for student in range(len(estudiantes)):
                        for value in range(student + 1, len(estudiantes)):
                            if estudiantes[student]['Nombre'] < estudiantes[value]['Nombre']:
                                estudiantes[student], estudiantes[value] = estudiantes[value], estudiantes[student]
            else:
                print("No se ha ingresado una opcion valida")

        elif isinstance(filter_by, str) and filter_by == 'Apellido':
            if option and option != 0:
                if isinstance(option, int) and option == 1:
                    for student in range(len(estudiantes)):
                        for value in range(student + 1, len(estudiantes)):
                            if estudiantes[student]['Apellido'] > estudiantes[value]['Apellido']:
                                estudiantes[student], estudiantes[value] = estudiantes[value], estudiantes[student]

                elif isinstance(option, int) and option == 2:
                    for student in range(len(estudiantes)):
                        for value in range(student + 1, len(estudiantes)):
                            if estudiantes[student]['Apellido'] < estudiantes[value]['Apellido']:
                                estudiantes[student], estudiantes[value] = estudiantes[value], estudiantes[student]
            else:
                print("No se ha ingresado una opcion valida")

        else:
            print("No se ha ingresado un filtro válido")
    else:
        print("Ninguna información ingresada")

    return estudiantes


def busqueda_binaria(array, inicio, final, alumno):
    """
    Funcion que realiza busqueda binaria del alumno en fución de su nombre
    """

    if inicio <= final:
        mitad = (inicio + final) // 2
        if array[mitad]['Nombre'] == alumno:
            return f'El estudiante {array[mitad]["Nombre"]} {array[mitad]["Apellido"]} se encuentra en la posicion {mitad} \n Promedio: {array[mitad]["Promedio"]} \n Edad: {array[mitad]["Edad"]} \n Grado: {array[mitad]["Grado"]} \n Grupo: {array[mitad]["Grupo"]} \n Número de lista: {array[mitad]["Número de lista"]}'
        elif array[mitad]['Nombre'] > alumno:
            return busqueda_binaria(array, inicio, mitad - 1, alumno)
        else:
            return busqueda_binaria(array, mitad + 1, final, alumno)
    else:
        return f"No se encontró el estudiante {alumno}"


ordenamiento = acomodar_list(estudiantes)

alumno = input("Ingrese el nombre del alumno a buscar: ")

resultado = busqueda_binaria(estudiantes, 0, len(
    estudiantes) - 1, alumno)


print(resultado)
