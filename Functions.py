# funkcja zwracająca kolejną liczbę pierwszą
# 1,2,3,5,7,11,....
# n=5 -> 11

# definicja funkcji


def getPrimaryNumbers(n=5):         # argument domyślny
    primaryNumbers = [1]
    number = 2
    while(len(primaryNumbers) < n):
        isPrimary = True
        for div in range(2,number):
            if(number % div == 0):       # sprawdzenie podzielności
                isPrimary = False
        if(isPrimary):
            primaryNumbers.append(number)
        number += 1
    return primaryNumbers, primaryNumbers[len(primaryNumbers)-1]

# wywołanie funkcji
element = 11
print("Lista:", getPrimaryNumbers(element)[0])
print(element,"element:", getPrimaryNumbers(element)[1])
print(getPrimaryNumbers())

from datetime import date
# https://docs.python.org/3/library/datetime.html
def printParameters(login, password, email, status=True, registrationDate=date.today()):
    return ("%s %s %s %s %s" % (login, password, email, status, registrationDate))

# różne wywołania
print(printParameters("mk","mk","mk"))           # tylko argumenty obowiązkowe
print(printParameters("mk1","mk1","mk1", registrationDate="2020-01-01"))                    # argumenty obowiązkowe + wybrany argument opcjonalny
print(printParameters(
    email="mk2",
    password="mk2",
    login="mk2",
    registrationDate="2020-01-01",
    status=False))      # wszystkie argumenty

def nonDefinedParameters(*elements):        # parametr gwiazdka -> przyjmuje dowolną liczbę argumentów
    sum = 0
    for elem in elements:
        sum += elem
    return sum/len(elements)

print(nonDefinedParameters(1))
print(nonDefinedParameters(5,4,6))
print(nonDefinedParameters(2,2,2,2))

def sortList(numbers):
    numbers.sort()
    return numbers
list = [3,2,5,4,6]
print(sortList(list))

def bubbleSort(elements, asc=True):
    # pętla iterująca po kolejnych próbach sortowania
    noProbes = 1
    for probe in range(len(elements)-1):      # determinujemy 5 prób w przypadku najgorszym
        isSorted = True
        for index,value in enumerate(elements):
            if(index == len(elements) - 1):
                break
            if((elements[index] > elements[index + 1]) and asc):  # porównywanie sąsiednich komórek
                isSorted = False
                elem = elements[index + 1]              # wydobycie elementu na ideksie i + 1 do zmiennej
                elements[index + 1] = elements[index]   # zamiana kolejności
                elements[index] = elem
            if ((elements[index] < elements[index + 1]) and not asc):  # porównywanie sąsiednich komórek
                isSorted = False
                elem = elements[index + 1]  # wydobycie elementu na ideksie i + 1 do zmiennej
                elements[index + 1] = elements[index]  # zamiana kolejności
                elements[index] = elem
        # print(noProbes, elements)
        if(isSorted):                                   # spr czy byliśmy w if z zamianą elementów
            break
        noProbes += 1
    return elements

import time
from datetime import datetime

print(bubbleSort([3,2,1,5,4,6,21,34,44,22,20,55]))
t_start = datetime.now().microsecond / 1000
list = [1,2,3,4,5,6,7,8,9,8,7,6,5,53,3,4,5,6,7,7,8,8,9,1,0,99,4,7,7,6,5]
print(bubbleSort(list, asc=False))
t_stop = datetime.now().microsecond / 1000
print(t_start)
print(t_stop)
print("czas wykonania funkcji w ms:", t_stop - t_start)







