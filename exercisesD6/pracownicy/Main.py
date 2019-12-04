from exercisesD6.pracownicy.controller.CompanyController import CompanyController
from exercisesD6.pracownicy.model.Employee import Employee
from exercisesD6.pracownicy.model.Trainee import Trainee

cc = CompanyController()
cc.addEmployeeOrTrainee(Employee("e1","e2","Junior DEV", 5000))
cc.addEmployeeOrTrainee(Employee("e1","e2","Junior DEV", 5000))
cc.addEmployeeOrTrainee("Pani Jadzia z gazowni")
cc.addEmployeeOrTrainee(Trainee("p1","p2"))
# cc.getEmployees()
# cc.getTraineeOrderByLogin()
# cc.getManagersAndHeadsOrderByLoginASC()
# cc.setPrise(1000, "eee1")
cc.changeEmployeeSalary("mk1",17000)
