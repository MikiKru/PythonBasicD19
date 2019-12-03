# klasa modelu determinuje strukturę danych
# wspiera podejście ORM - Obiject Relationship Mapping
# rzutuje cechy danych pochodzące z tabelki SQL na obiekt Python
class Student:
    # konstruktor klasy
    def __init__(self, index, name, lastname):
        self.index = index
        self.name = name
        self.lastname = lastname
        self.grades = []
    # metoda do dodawania ocen do listy grades
    def addGrade(self, grade):
        self.grades.append(grade)
    # metoda zwracająca średnią ocen studenta
    def calculateAVG(self):
        cumSum = 0
        if (len(self.grades)==0):
            return 0
        for grade in self.grades:
            cumSum += grade
        return cumSum/len(self.grades)
    def __str__(self):
        return "| %6s | %15s | %15s | %20s | %7s |" % \
               (self.index, self.name, self.lastname, self.grades,
                "B/D" if self.calculateAVG() == 0 else round(self.calculateAVG(),2))

# testowanie modelu
# s = Student(123123,"test","test")
# print(s)
# s.addGrade(5)
# s.addGrade(2)
# s.addGrade(3)
# print(s)