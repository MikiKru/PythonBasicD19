# Kontroller -> klasa obsługi żądań użytkownika pochodzących
# z widoku (html, cli, window)
# Implementuje logikę aplikacji
from exercisesD5.P67.model.Student import Student


class StudentController:
    students = []
    # metoda dodającą studenta do listy
    def addStudent(self, index, name, lastname):
        if(self.validateStudentIndex(index)):   # wywołanie walidacji
            # utworznie obiektu studenta -> odwołanie do modelu
            s = Student(index, name, lastname)
            self.students.append(s)
            print("Dodano:", s)
        else:
            print("Istnieje student o wskazanym indeksie")
    # metoda do walidacji danych studenta
    def validateStudentIndex(self,inputIndex):
        for student in self.students:
            if(student.index == inputIndex):
                # jeżeli już występuje taki index
                return False    # nie dodajemy do listy
        return True             # dodajemy do listy
    # metoda dodająca ocenę
    def addGradeToStudent(self,inputIndex, grade):
        gradesTemplate = [2,3,3.5,4,4.5,5,5.5]
        if(grade in gradesTemplate):
            isAdded = False
            for student in self.students:
                if (student.index == inputIndex):
                    isAdded = True
                    student.addGrade(grade)
                    print("DODANO OCENĘ")
            # wypisz zaktualizowaną listę studentów
            if(isAdded == False):
                print("Nie ma studenta o takim indeksie")
            self.getStudents()
        else:
            print("Podałeś niepoprawną ocenę")
    # metoda do usuwania studenta po indeksie
    def deleteStudentByIndex(self, inputIndex):
        for student in self.students:
            if(student.index == inputIndex):
                print("Usunięto", student)
                self.students.remove(student)
        self.getStudents()
    # metoda wypisująca wszystkich studentów z listy students
    def getStudents(self):
        print("| %6s | %15s | %15s | %20s | %7s |"
              % ("INDEKS", "IMIĘ", "NAZWISKO","OCENY","ŚREDNIA"))
        for student in self.students:
            print(student)

# testowanie kontrolera
sc = StudentController()
sc.addStudent(123123, "test","test")
sc.addStudent(123123, "test2","test2")
sc.getStudents()
sc.addGradeToStudent(123123,4)
sc.addGradeToStudent(123123,3)
sc.addGradeToStudent(123121,3)  # blad danych
sc.addGradeToStudent(123123,33)  # blad danych
sc.deleteStudentByIndex(123123)





