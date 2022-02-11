students = [
    {'name': 'Ale', 'lastname': 'Azuela', 'grades': 10, 'age': 18},
    {'name': 'Luis', 'lastname': 'Cedillo', 'grades': 8, 'age': 19},
    {'name': 'Aitana', 'lastname': 'Luaces', 'grades': 10, 'age': 20},
]


def sort_json(students):

    filter_by = str(input("Elige el filtro que quieres utilizar: "))

    option = int(
        input("1. Ordenar de menor a mayor\n2. Ordenar de mayor a menor\nIngrese una opcion: "))

    if filter_by:
        if isinstance(filter_by, str) and filter_by == 'grades' and filter_by != "":
            if option and option != 0:
                if isinstance(option, int) and option == 1:
                    for student in range(len(students)):
                        for value in range(student + 1, len(students)):
                            if students[student]['grades'] > students[value]['grades']:
                                students[student], students[value] = students[value], students[student]

                elif isinstance(option, int) and option == 2:
                    for student in range(len(students)):
                        for value in range(student + 1, len(students)):
                            if students[student]['grades'] < students[value]['grades']:
                                students[student], students[value] = students[value], students[student]
            else:
                print("No se ha ingresado una opcion valida")
        elif isinstance(filter_by, str) and filter_by == 'age' and filter_by != "":
            if option and option != 0:
                if isinstance(option, int) and option == 1:
                    for student in range(len(students)):
                        for value in range(student + 1, len(students)):
                            if students[student]['age'] > students[value]['age']:
                                students[student], students[value] = students[value], students[student]

                elif isinstance(option, int) and option == 2:
                    for student in range(len(students)):
                        for value in range(student + 1, len(students)):
                            if students[student]['age'] < students[value]['age']:
                                students[student], students[value] = students[value], students[student]
            else:
                print("No se ha ingresado una opcion valida")
        elif isinstance(filter_by, str) and filter_by == 'name' and filter_by != "":
            if option and option != 0:
                if isinstance(option, int) and option == 1:
                    for student in range(len(students)):
                        for value in range(student + 1, len(students)):
                            if students[student]['name'] > students[value]['name']:
                                students[student], students[value] = students[value], students[student]

                elif isinstance(option, int) and option == 2:
                    for student in range(len(students)):
                        for value in range(student + 1, len(students)):
                            if students[student]['name'] < students[value]['name']:
                                students[student], students[value] = students[value], students[student]
            else:
                print("No se ha ingresado una opcion valida")
            if option and option != 0:
                if isinstance(option, int) and option == 1:
                    for student in range(len(students)):
                        for value in range(student + 1, len(students)):
                            if students[student]['name'] > students[value]['name']:
                                students[student], students[value] = students[value], students[student]

                elif isinstance(option, int) and option == 2:
                    for student in range(len(students)):
                        for value in range(student + 1, len(students)):
                            if students[student]['name'] < students[value]['name']:
                                students[student], students[value] = students[value], students[student]
            else:
                print("No se ha ingresado una opcion valida")
        elif isinstance(filter_by, str) and filter_by == 'lastname' and filter_by != "":
            if option and option != 0:
                if isinstance(option, int) and option == 1:
                    for student in range(len(students)):
                        for value in range(student + 1, len(students)):
                            if students[student]['lastname'] > students[value]['lastname']:
                                students[student], students[value] = students[value], students[student]

                elif isinstance(option, int) and option == 2:
                    for student in range(len(students)):
                        for value in range(student + 1, len(students)):
                            if students[student]['lastname'] < students[value]['lastname']:
                                students[student], students[value] = students[value], students[student]
            else:
                print("No se ha ingresado una opcion valida")
        else:
            print("No se ha ingresado un filtro válido")
    else:
        print("Ninguna información ingresada")

    return students


result = sort_json(students)

print(result)
