
numlist = []

number = int(input("Ingrese un numero para la longitud de la lista: "))

for i in range(number):
    value = int(input("Ingrese el valor del elemento %d: " % i))
    numlist.append(value)
# Sort the numbers in the list


def sort(numlist):

    option = int(
        input("1. Ordenar de menor a mayor\n2. Ordenar de mayor a menor\nIngrese una opcion: "))

    if option and option != 0:
        if isinstance(option, int) and option == 1:
            for i in range(len(numlist)):
                for j in range(i + 1, len(numlist)):
                    if numlist[i] > numlist[j]:
                        numlist[i], numlist[j] = numlist[j], numlist[i]

        elif isinstance(option, int) and option == 2:
            for i in range(len(numlist)):
                for j in range(i + 1, len(numlist)):
                    if numlist[i] < numlist[j]:
                        numlist[i], numlist[j] = numlist[j], numlist[i]

    elif option == None or option == "" or option == 0:
        print("No ha ingresado ningun valor")

    else:
        print("No se ha ingressado una opcion valida")

    return numlist


result = sort(numlist)

print(result)
