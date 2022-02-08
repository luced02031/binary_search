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
                    for i in range(len(students)):
                        for j in range(i + 1, len(students)):
                            if students[i]['grades'] > students[j]['grades']:
                                students[i], students[j] = students[j], students[i]

                elif isinstance(option, int) and option == 2:
                    for i in range(len(students)):
                        for j in range(i + 1, len(students)):
                            if students[i]['grades'] < students[j]['grades']:
                                students[i], students[j] = students[j], students[i]
            else:
                print("No se ha ingresado una opcion valida")
        elif isinstance(filter_by, str) and filter_by == 'age' and filter_by != "":
            if option and option != 0:
                if isinstance(option, int) and option == 1:
                    for i in range(len(students)):
                        for j in range(i + 1, len(students)):
                            if students[i]['age'] > students[j]['age']:
                                students[i], students[j] = students[j], students[i]

                elif isinstance(option, int) and option == 2:
                    for i in range(len(students)):
                        for j in range(i + 1, len(students)):
                            if students[i]['age'] < students[j]['age']:
                                students[i], students[j] = students[j], students[i]
            else:
                print("No se ha ingresado una opcion valida")
        elif isinstance(filter_by, str) and filter_by == 'name' and filter_by != "":
            if option and option != 0:
                if isinstance(option, int) and option == 1:
                    for i in range(len(students)):
                        for j in range(i + 1, len(students)):
                            if students[i]['name'] > students[j]['name']:
                                students[i], students[j] = students[j], students[i]

                elif isinstance(option, int) and option == 2:
                    for i in range(len(students)):
                        for j in range(i + 1, len(students)):
                            if students[i]['name'] < students[j]['name']:
                                students[i], students[j] = students[j], students[i]
            else:
                print("No se ha ingresado una opcion valida")
            if option and option != 0:
                if isinstance(option, int) and option == 1:
                    for i in range(len(students)):
                        for j in range(i + 1, len(students)):
                            if students[i]['name'] > students[j]['name']:
                                students[i], students[j] = students[j], students[i]

                elif isinstance(option, int) and option == 2:
                    for i in range(len(students)):
                        for j in range(i + 1, len(students)):
                            if students[i]['name'] < students[j]['name']:
                                students[i], students[j] = students[j], students[i]
            else:
                print("No se ha ingresado una opcion valida")
        elif isinstance(filter_by, str) and filter_by == 'lastname' and filter_by != "":
            if option and option != 0:
                if isinstance(option, int) and option == 1:
                    for i in range(len(students)):
                        for j in range(i + 1, len(students)):
                            if students[i]['lastname'] > students[j]['lastname']:
                                students[i], students[j] = students[j], students[i]

                elif isinstance(option, int) and option == 2:
                    for i in range(len(students)):
                        for j in range(i + 1, len(students)):
                            if students[i]['lastname'] < students[j]['lastname']:
                                students[i], students[j] = students[j], students[i]
            else:
                print("No se ha ingresado una opcion valida")
        else:
            print("No se ha ingresado un filtro válido")
    else:
        print("Ninguna información ingresada")

    return students


result = sort_json(students)

print(result)
