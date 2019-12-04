from exercisesD6.pracownicy.model.Employee import Employee, Permission
from exercisesD6.pracownicy.model.Trainee import Trainee

class CompanyController:
    employees = [
        Employee("mk1","mk1","PYTHON DEV",11000,Permission.ROLE_EMPL),
        Employee("mk2","mk2","JAVA DEV",9000,Permission.ROLE_EMPL),
        Employee("mk3","mk3","PYTHON DEV",12000,Permission.ROLE_EMPL),
        Employee("mk4","mk4","MANAGER",14000,Permission.ROLE_MAN),
        Employee("mk5","mk5","SCRUM MASTER",13000,Permission.ROLE_MAN),
        Employee("mk6","mk6","HEAD",17000,Permission.ROLE_HEAD),
        Employee("mk7","mk7","HEAD",21000,Permission.ROLE_HEAD),
        Employee("mk8","mk8","DEV OPS",11500,Permission.ROLE_EMPL),
        Trainee("t1", "t1"),
        Trainee("t2","t2"),
        Trainee("t3","t3")
    ]
    #1. dodawanie pracownika lub praktykanta z unikatowym loginem
    def addEmployeeOrTrainee(self, o):
        if(o.__class__.__name__ == "Trainee" or o.__class__.__name__ == "Employee"):
            if(self.loginValid(o.login)):
                print("Dodano pracownika", o.login, o.possition)
                self.employees.append(o)
            else:
                print("Istnieje już taki login w naszej bazie danych")
        else:
            print("Dany obiekt nie jest pracownikiem ani praktykantem")
    # 1* sprawdzenie czy dany login nie istnieje w liście employees
    def loginValid(self, login):
        for e in self.employees:
            if(e.login == login):
                return False
        return True
    #2. wyświetlenie wszystkich pracowników i praktykantów posortowanych po pensji DESC
    def getEmployees(self):
        # sortowanie po pensji
        for e in sorted(self.employees, key=lambda e : e.salary, reverse=True):
            print(e)
    #3. wyświetlenie tylko kierowników lub dyrektorów posortowanych po loginie A-Z
    def getManagersAndHeadsOrderByLoginASC(self):
        result = filter(lambda e : e.__class__.__name__ == "Employee" and e.permission.value in [2,3],
                        self.employees)
        for i in sorted(result, key=lambda e:e.login, reverse=False):
            print(i)
        # for e in self.employees:
        #     if(e.__class__.__name__ == "Employee"):
        #         if(e.permission.value in [2,3]):
        #             print(e)

    #4. wyświetlenie praktykantów posortowanych po loginie Z-A
    def getTraineeOrderByLogin(self):
        # filtruje liste pracowników i zwraca tylko praktykantów
        result = filter(lambda e : e.__class__.__name__ == "Trainee", self.employees)
        for t in sorted(result,key=lambda t : t.login, reverse=True):
            print(t)
    # przypisanie nagrody do pracownika lub praktykanta

    # zmiana pensji tylko dla pracownika

    # usuwanie pracownika lub praktykanta z listy

