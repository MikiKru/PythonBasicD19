import exercisesD7.sql.database_credentials as secret
from exercisesD7.database_app.model.User import User
import pymysql


class TaskManagerController:
    users = []      # koresponduje z rekordami w tabelce user
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



