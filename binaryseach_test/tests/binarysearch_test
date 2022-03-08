# Clasificación de los datos

students = [
    {'name': 'Ale', 'lastname': 'Perez', 'grades': 10, 'age': 20, 'id': 1},
    {'name': 'Bernarndo', 'lastname': 'Perez', 'grades': 20, 'age': 30, 'id': 2},
    {'name': 'Carlos', 'lastname': 'Perez', 'grades': 30, 'age': 40, 'id': 3},
    {'name': 'Daniel', 'lastname': 'Perez', 'grades': 40, 'age': 50, 'id': 4},
    {'name': 'Ernesto', 'lastname': 'Perez', 'grades': 50, 'age': 60, 'id': 5}

]


def binarysearch(array, start, end, objective):
    if start > end:
        return f'{objective} not found'
    else:
        mid = (start + end) // 2
        if array[mid]['name'] == objective:
            return f'the student {objective} {array[mid]["lastname"]} is in the array at position {mid}, with grades {array[mid]["grades"]}, and age {array[mid]["age"]}'
        elif array[mid]['name'] > objective:
            return binarysearch(array, start, mid - 1, objective)
        else:
            return binarysearch(array, mid + 1, end, objective)


student_input = str(input("Enter a name from the list: "))

search_result = binarysearch(students, 0, len(students) - 1, student_input)

print(search_result)
