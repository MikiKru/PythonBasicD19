class User:
    def __init__(self, email, password, name, lastname, gender, user_id=0):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.name = name
        self.lastname = lastname
        self.gender = gender
    def __str__(self):
        return "| %2d | %15s | %15s | %15s | %15s | %2s |" % \
               (self.user_id,self.email, self.password, self.name,
               self.lastname, self.gender)