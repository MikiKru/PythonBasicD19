import exercisesD7.sql.database_credentials as secret
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
