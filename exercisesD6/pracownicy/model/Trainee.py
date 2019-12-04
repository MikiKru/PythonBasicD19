import hashlib
class Trainee:
    def __init__(self, login, password):
        self.login = login
        self.password = hashlib.md5(("salt:XYZ"+password).encode('utf-8')).hexdigest() # 0-9abcdef
        self.possition = "PRAKTYKANT"
        self.salary = 0
    def assignPrise(self, amount):
        self.salary += amount
    def __str__(self):
        return "| %15s | %10s | %15s | %13.2fzł |" % \
        (self.login, self.password[0:8], self.possition, self.salary)

# #test
# t = Trainee("MichałK","qwe123")
# t.assignPrise(-1000)
# print(t)

