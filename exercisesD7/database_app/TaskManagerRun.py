from exercisesD7.database_app.controller.TaskManagerController import TaskManagerController

start = TaskManagerController()
start.insertUser("mk@mk.pl","mk","Michal", "Kruczkowski", "M")
start.selectUsers()