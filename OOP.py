from datetime import date


class Auto:
    # pola klasowe -> obiekty, zmienne
    brand = "b/d"
    model = "b/d"
    # metody klasowe -> funkcje
    def helloInClass(self):
        return "Witaj w programowaniu obiektowym"

# utworzenie obiektu
a = Auto()
print(a.helloInClass())
a.brand = "BMW"
a.model = "X3"
print(a.brand, a.model)
a1 = Auto()
print(a1.brand, a1.model)

class User:
    def __init__(self,login, password, status, registrationDate):     # metoda wywoływana jako pierwsza po utworzeniu obieku
        # pole kalsowe są inicjalizowane wartościami z argumentu funkcji
        self.login = login
        self.password = password
        self.status = status
        self.registrationDate = registrationDate
    def setStatus(self, status):    # modyfikacja statusu na wartość podaną w argumencie
        self.status = status
    # funkcje specjalne - wszystkie te rozpoczynające się od __
    def __str__(self):  # funkcja wywoływana gdy obiket jest rzutowany do napisu
        return ("| %10s | %10s | %8s | %10s |" % (self.login, self.password, self.status, self.registrationDate))

u1 = User("mk@mk.pl","mk",True,date.today())
print(u1.login, u1.password, u1.status, u1.registrationDate)
u2 = User("kk@kk.pl","kk",False,date.today())
print(u2.login, u2.password, u2.status, u2.registrationDate)
u3 = u2
print("Przed",u2.status, u3.status)
u2.status = True
print("Po",u2.status, u3.status)
u1.setStatus(False)
print(u1)
print(u2)
print(u3)




