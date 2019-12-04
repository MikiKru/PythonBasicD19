class Trainee:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.possition = "PRAKTYKANT"
        self.salary = 0
    def assignPrise(self, amount):
        self.salary = amount
    def __str__(self):
        return "| %15s | %15s | %15s | %13.2fzł |" % \
        (self.login, 10 * "*", self.possition, self.salary)

#test
t = Trainee("MichałK","qwe123")
t.assignPrise(-1000)
print(t)

