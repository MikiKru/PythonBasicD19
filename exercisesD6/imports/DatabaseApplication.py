# importy są adresowane od katalogu domowego -> nazwa projektu
# nazwa modułu występuje bez rozszerzenia
# alias zastępuję wszystko co jest w adresie modułu razem z jego nazwą
import exercisesD6.imports.SecretVariables as sv
# dostęp do zmiennych
print(sv.database)
print(sv.username)
print(sv.password)
print(sv.host)
print(sv.port)
# dostęp do metod
print(sv.getConnection())
# dostęp do klas
