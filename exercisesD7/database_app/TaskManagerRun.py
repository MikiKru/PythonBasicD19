from exercisesD7.database_app.controller.TaskManagerController import TaskManagerController

start = TaskManagerController()
# start.insertUser("kk@kk.pl","mk","Karol", "Karol", "M")
start.selectUsers()
# start.insertTaskToUser("programowanie", "programowanie w Python", "nowe", "2020-01-01", 2)
start.selectTasks()
start.selectSummary()