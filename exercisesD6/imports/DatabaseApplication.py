# importy są adresowane od katalogu domowego -> nazwa projektu
# nazwa modułu występuje bez rozszerzenia
# alias zastępuję wszystko co jest w adresie modułu razem z jego nazwą
import exercisesD6.imports.SecretVariables as sv
import random as rnd

for i in dir(rnd):
    print(i)

help(rnd)
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

