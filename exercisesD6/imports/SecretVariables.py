database = "python_db"
username = "root"
password = "123"
port = 3306
host = "localhost"

def getConnection():
    return "connected"

class Hello:
    def __init__(self, name):
        ''' Inicjalizacja zmienna imię @author '''
        self.name = name
    def __str__(self):
        return "Hello %s" % (self.name)

# # uruchomienie skryptu
# h = Hello("x")
# print(h)