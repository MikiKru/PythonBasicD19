from exercisesD7.database_app.controller.TaskManagerController import TaskManagerController

start = TaskManagerController()
# start.insertUser("kk@kk.pl","mk","Karol", "Karol", "M")
# start.selectUsers()
# start.insertTaskToUser("programowanie", "programowanie w Python", "nowe", "2020-01-01", 2)
# start.selectTasks()
# start.selectSummary()
# start.updateTaskDateStop(1,"2020-05-05")
# start.deleteTaskById(1)
start.insertSubtaskToTask("obiektowość", "2019-12-14",'otwarte', 2)
start.insertSubtaskToTask("dziedziczenie", "2019-12-19",'otwarte', 2)
start.selectSummary()