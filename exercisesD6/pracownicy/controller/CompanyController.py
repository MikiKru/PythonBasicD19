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

    #2. wyświetlenie wszystkich pracowników i praktykantów posortowanych po pencji DESC

    # przypisanie nagrody do pracownika lub praktykanta

    # zmiana pensji tylko dla pracownika

    # usuwanie pracownika lub praktykanta z listy

    # wyświetlenie tylko kierowników

    # wyświetlenie praktykantów