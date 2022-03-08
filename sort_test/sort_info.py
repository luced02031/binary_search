from unittest import result


students1 = [
    {'name': 'Ale', 'lastname': 'Azuela', 'grades': 10, 'age': 18},
    {'name': 'Luis', 'lastname': 'Cedillo', 'grades': 8, 'age': 19},
    {'name': 'Aitana', 'lastname': 'Luaces', 'grades': 10, 'age': 20},
]

# Create a function that sorts the students by their name


def sort_students(students):

    option = str(input("Enter the option you want to sort by: "))
    reverse = str(input("Do you want to reverse the order? (y/n): "))

    if option == 'name' and reverse == "n":
        return sorted(students, key=lambda student: student['name'])
    elif option == 'name' and reverse == "y":
        return sorted(students, key=lambda student: student['name'], reverse=True)
    elif option == 'age' and reverse == "n":
        return sorted(students, key=lambda student: student['age'])
    elif option == 'age' and reverse == "y":
        return sorted(students, key=lambda student: student['age'], reverse=True)
    elif option == 'grades' and reverse == "n":
        return sorted(students, key=lambda student: student['grades'])
    elif option == 'grades' and reverse == "y":
        return sorted(students, key=lambda student: student['grades'], reverse=True)
    else:
        return "Invalid option"


result = sort_students(students1)

print(result)
