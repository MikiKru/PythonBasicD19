import exercisesD7.sql.database_credentials as secret
from exercisesD7.database_app.model.Subtask import Subtask
from exercisesD7.database_app.model.Task import Task
from exercisesD7.database_app.model.User import User
import pymysql


class TaskManagerController:
    def __init__(self):
        self.connection = pymysql.connect(
            host=secret.host,
            user=secret.username,
            password=secret.password,
            db=secret.database_name,
            charset='utf8'
        )
        print("...CONNECTED...")
        self.cursor = self.connection.cursor()

    def insertUser(self, email, password, name, lastname, gender):
        u = User(email,password,name,lastname,gender)
        # wykoananie polecenia SQL -> nie zwraca waniku
        self.cursor.execute("INSERT INTO user VALUES (default, %s, %s, %s, %s, %s)",
                            (u.email, u.password, u.name, u.lastname, u.gender))
        # decision = input("czy na pewno chcesz dodać:" + u.email + "(T/N)").upper()
        self.connection.commit()
        print("DODANO", u.email)
        # if(decision == "T"):
        #     self.connection.commit()    # potwierdzenie strasakcji
        #     print("DODANO", u.email)
        # else:
        #     self.connection.rollback()    # odrzucenie transakcji
        #     print("NIE DODANO", u.email)
    def selectUsers(self):
        # wykoanie zapytania SQL -> zwraca wynik
        self.cursor.execute("SELECT * FROM user")
        result = self.cursor.fetchall()     # pobieramy wszystkie wyniki
        for row in result:
            u = User(row[1], row[2], row[3], row[4], row[5], row[0])
            print(u)
    def insertTaskToUser(self, name, description, status, date_stop, user_id):
        t = Task(name, description,status,date_stop,user_id)
        self.cursor.execute("INSERT INTO task VALUES (default, %s, %s, %s, default, %s, %s)",
                            (t.name, t.description, t.status, t.date_stop, t.user_id))
        self.connection.commit()
        print("DODANO ZADANIE",t.name)
    def selectTasks(self):
        self.cursor.execute("SELECT * FROM task")
        for row in self.cursor.fetchall():
            t = Task(row[1],row[2],row[3],row[5],row[6],row[0],row[4])
            print(t)
    def selectSummary(self):
        self.cursor.execute("SELECT * FROM summary")
        print("| %20s | %20s | %20s | %20s | %20s | %20s | %20s |" %
              ("ZADANIE","STATUS","PODZADANIE","DEADLINE","STATUS","IMIE","NAZWISKO"))
        for row in self.cursor.fetchall():
            print("| %20s | %20s | %20s | %20s | %20s | %20s | %20s |" %
                  (row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
    def updateTaskDateStop(self, task_id, newDeadline):
        self.cursor.execute("UPDATE task SET date_stop = %s WHERE task_id = %s", (newDeadline,task_id))
        self.connection.commit()
        self.selectTasks()
    def deleteTaskById(self, task_id):
        self.cursor.execute("DELETE FROM task WHERE task_id = %s" , task_id)
        self.connection.commit()
        print("USUNIĘTO")
        self.selectTasks()
    def insertSubtaskToTask(self, detail_description, deadline, status, task_id):
        s = Subtask(detail_description,deadline,status,task_id)
        self.cursor.execute("INSERT INTO subtask VALUES (default, %s, %s, %s, %s)",
                            (s.detail_description,s.deadline,s.status,s.task_id))
        print("DODANO SUBTASK",s.detail_description)
        self.connection.commit()



