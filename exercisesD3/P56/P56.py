def isGrade(grade):
    return grade in gradesTemplate
def gradesAvg(grades):
    sum = 0
    for grade in grades:
        sum += grade
    return 0 if len(grades) == 0 else sum / len(grades)

gradesTemplate = (3.0, 3.5, 4.0, 4.5, 5.0)
students = {
            "1" : ["M","K", [] ],
            "2" : ["K","K", [] ],
            "3" : ["X","X", [] ]
}
while(True):
    for student in students.keys():
        print("| %3s | %10s | %10s | %20s | %8.2f |"
              % (student,students[student][0],
                 students[student][1],
                 students[student][2],
                 gradesAvg(students[student][2])))
    id = input("Wybierz studenta (ENTER - wyjście)")
    if(id == ""):
        break
    if(id not in students.keys()):
        print("Nie ma takiego studenta")
        continue
    try:
        grade = float(input("Wprowadź ocenę:"))
    except:
        print("Ocena musi być liczbą!")
    if(not isGrade(grade)):
        print("Nie ma takie oceny w skali ocen!")
        continue
    students[id][2].append(grade)




