# importy są adresowane od katalogu domowego -> nazwa projektu
# nazwa modułu występuje bez rozszerzenia
# alias zastępuję wszystko co jest w adresie modułu razem z jego nazwą
import exercisesD6.imports.SecretVariables as sv
import random as rnd

# for i in dir(rnd):
#     print(i)
#
# help(rnd)
# # dostęp do zmiennych
# print(sv.database)
# print(sv.username)
# print(sv.password)
# print(sv.host)
# print(sv.port)
# # dostęp do metod
# print(sv.getConnection())
# # dostęp do klas
# obiektKlasyZaimportowanej = sv.Hello("Michał")
# print(obiektKlasyZaimportowanej.name)
# print(obiektKlasyZaimportowanej)

import os

print("Direct ref", os.getcwd())
print("Direct ref", "D:\\Szkolenia\\Programowanie\\PWN\\DataAnalyst\\Projects\\PythonBasicD19\\exercisesD6\\imports\\DatabaseApplication.py")

print("W katalogu w którym się znajdujemy aktualnie:")
for i in os.listdir('.'):
    print(i)


print("W katalogu pracowników jest oś takiego")
for i in os.listdir('D:\\Szkolenia\\Programowanie\\PWN\\DataAnalyst\\Projects\\PythonBasicD19\\exercisesD6\\pracownicy'):
    print(i)

import re

os.chdir("C:\\Users\\PROXIMO\\Desktop") # change directory
for file in os.listdir('.'):    # list directory w aktualnej lokalizacji
    print(file)


