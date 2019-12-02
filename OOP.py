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
    def __init__(self,login, password, status, registrationDate=date.today()):     # metoda wywoływana jako pierwsza po utworzeniu obieku
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
    # def __del__(self):
    #     print("Obiekt %s jest usunięty" % (self))

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
print(u1.__class__.__name__)
print(type(u1))

u4 = User("x","x",True)
u5 = User("x","x",True, registrationDate="2000-02-02")
print(u4)
# print(u5.__del__())
# print(u5)


# Napisz program OOP, który reprezentuje składowe barw RGB
# R - red 0-255
# G - green
# B - blue
# Implementacja klasy modelu reprezentującej dowolny kolor [r,g,b]
class RGB:
    def __init__(self, r,g,b):
        if(r >= 0 and g >= 0 and b >= 0 and r <= 255 and g <= 255 and b <= 255):
            self.r = r
            self.g = g
            self.b = b
        else:
            print("Podane wartości nie są poprawne")
            self = None
    def __add__(self, other):
        # utworzenie nowego obiektu na podstawei sumy składowych r g i b z dwóch kolorów
        c = RGB(self.r + other.r, self.g + other.g, self.b + other.b)
        return c
    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b
    def __str__(self):
        return "[%d,%d,%d]" % (self.r, self.g, self.b)

red = RGB(255, 0,0)
green = RGB(0, 255,0)
yellow = RGB(255, 255,0)
badColour = RGB(333,0,0)
mixed = red.__add__(green)
print(type(mixed))
print(red, green, yellow, mixed, (red + green))
print("czy czerwony to zielony:",red == green)
print("czy zółty to samo co czerwony + zielony:", ("tak" if (yellow == (red + green)) else "nie"))













