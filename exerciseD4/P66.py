# inicjalizacja wartości globalnej w skrypcie
globalId = 0
class Player:
    def __init__(self, name, lastname, repr, weight, height):
        self.name = name
        self.lastname = lastname
        self.repr = repr
        self.weight = weight
        self.height = height
        global globalId     # modyfiakcja wartości globalnej w skrypcie
        globalId += 1       # global -> wskażnik globalny niezwiązany z klasą Player
        self.id = globalId  # self -> id dla konkretnego obiektu
    def calculateBMI(self):
        return self.weight/pow(self.height/100,2)
    def __str__(self):
        return ("| %3d | %10s | %10s | %10s | %10d | %10d | %10.2f |"
                % ( self.id,
                    self.name,
                    self.lastname,
                    self.repr,
                    self.weight,
                    self.height,
                    self.calculateBMI()))
p1 = Player("Adam","Małysz","POL",50, 165)
p2 = Player("Kamil","Stoch","POL",60, 180)
p3 = Player("Jan","Matura","CZE",60, 180)
p4 = Player("Martin","Shmidt","GER",60, 180)

players = [p1,p2,p3,p4]
for player in players:
    print(player)





