import time
# Json de información de estudiantes

estudiantes = [
    {
        'Nombre': 'Luis', 'Apellido': 'Cedillo', 'Edad': '19', 'Grado': '6to', 'Grupo': 'CCH - B', 'Promedio': 8.2, 'Número de lista': '1'
    },
    {
        'Nombre': 'Aitana', 'Apellido': 'Luaces', 'Edad': '18', 'Grado': '6to', 'Grupo': 'CCH - B', 'Promedio': 6.7, 'Número de lista': '2'
    },
    {
        'Nombre': 'Alejandra', 'Apellido': 'Azuela', 'Edad': '18', 'Grado': '6to', 'Grupo': 'CCH - B', 'Promedio': 1, 'Número de lista': '3'
    },
    {
        'Nombre': 'Fernanda', 'Apellido': 'Coldado', 'Edad': '18', 'Grado': '6to', 'Grupo': 'CCH - B', 'Promedio': 7.8, 'Número de lista': '4'

    },
    {
        'Nombre': 'Valeria Alejandra', 'Apellido': 'Carrillo', 'Edad': '17', 'Grado': '6to', 'Grupo': 'CCH - B', 'Promedio': 4.3, 'Número de lista': '5'
    },
    {
        'Nombre': 'Alexandra', 'Apellido': 'El-Khalili', 'Edad': '18', 'Grado': '6to', 'Grupo': 'CCH - B', 'Promedio': 2.1, 'Número de lista': '6'
    },
    {
        'Nombre': 'Ligia', 'Apellido': 'Cortes', 'Edad': '18', 'Grado': '6to', 'Grupo': 'CCH - B', 'Promedio': 3.65, 'Número de lista': '7'
    },
    {
        'Nombre': 'Derek', 'Apellido': 'Emilio', 'Edad': '17', 'Grado': '6to', 'Grupo': 'CCH - B', 'Promedio': 7.2, 'Número de lista': '8'
    },
    {
        'Nombre': 'Natalie', 'Apellido': 'Gonzalez', 'Edad': '17', 'Grado': '6to', 'Grupo': 'CCH - B', 'Promedio': 10, 'Número de lista': '9'
    },
    {
        'Nombre': 'Aldo', 'Apellido': 'Solorio', 'Edad': '18', 'Grado': '6to', 'Grupo': 'CCH - B', 'Promedio': 9.3, 'Número de lista': '10'
    },
    {
        'Nombre': 'Ana', 'Apellido': 'Galicia', 'Edad': '17', 'Grado': '6to', 'Grupo': 'CCH - B', 'Promedio': 9.5, 'Número de lista': '11'
    },
    {
        'Nombre': 'Regina', 'Apellido': 'Ocaña', 'Edad': '18', 'Grado': '6to', 'Grupo': 'CCH - B', 'Promedio': 9.3, 'Número de lista': '12'
    }
]

# función que muestre estudiante en archivo de excel


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

    # Si el inicio es menor o igual al final, se realiza la busqueda
    if inicio <= final:
        # Se obtiene el valor medio mediante la suma de inicio y final
        mitad = (inicio + final) // 2

        # Si el valor medio es igual al alumno, se retorna el indice más su información
        if array[mitad]['Nombre'] == alumno:
            return f'''El estudiante {array[mitad]["Nombre"]} {array[mitad]["Apellido"]} se encuentra en la posicion {mitad} 
            \n Promedio: {array[mitad]["Promedio"]} \n Edad: {array[mitad]["Edad"]} \n Grado: {array[mitad]["Grado"]} 
                \n Grupo: {array[mitad]["Grupo"]} \n Número de lista: {array[mitad]["Número de lista"]}'''

        # Si el valor medio es mayor al alumno, se realiza la busqueda en el primer subarreglo y se actualiza el inicio al valor medio
        elif array[mitad]['Nombre'] > alumno:
            return busqueda_binaria(array, inicio, mitad - 1, alumno)

        # Si el valor medio es menor al alumno, se realiza la busqueda en el segundo subarreglo y se actualiza el final al valor medio
        else:
            return busqueda_binaria(array, mitad + 1, final, alumno)

    # Si el inicio es mayor al final, se retorna un mensaje de que el alumno no se encuentra en el arreglo
    else:
        return f"No se encontró el estudiante {alumno}"


# Muestra cuantos ciclos se han ejecutado en la busqueda binaria



def busqueda_lineal(array, alumno):
    """
    Funcion que realiza busqueda lineal del alumno en fución de su nombre
    """

    # Se hace un recorrido por cada elemento del arreglo
    for student in array:

        # Si el nombre del alumno es igual al nombre del estudiante, se retorna el indice más su información
        if student['Nombre'] == alumno:
            return f'''El estudiante {student["Nombre"]} {student["Apellido"]} se encuentra en la posicion {array.index(student)} \n Promedio: {student["Promedio"]}
                    \n Edad: {student["Edad"]} \n Grado: {student["Grado"]} \n Grupo: {student["Grupo"]} \n Número de lista: {student["Número de lista"]}'''

    # Si el nombre del alumno no es igual al nombre del estudiante, se retorna un mensaje de que el alumno no se encuentra en el arreglo
    return f"No se encontró el estudiante {alumno}"


ordenamiento, alumno = (acomodar_list(estudiantes),
                        input("Ingrese el nombre del alumno: "))


print(busqueda_binaria(estudiantes, 0, len(
    estudiantes) - 1, alumno))

# print(busqueda_lineal(estudiantes, alumno))
