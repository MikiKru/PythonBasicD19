# Utwórz listę wartości losowych naturalnych z zakresu 1 : 100
import random

randomList = []
for i in range(10):
    randomList.append(random.randint(1,10))
print(randomList)

# wyszukaj element z listy i zwróć jego indeks
# jeżeli elementu nie ma na liście to zwróć -1
find = int(input("podaj liczbę z zakresu od 1 do 10"))
# sprawdzamy czy eleemnt występuje w liście
if(find not in randomList):
    print("Element %i nie występuje w liście" % find)
else:
    for index, value in enumerate(randomList):
        if(value == find):
            print("Element %i znajduje się na indeksie %i" % (find, index))
            break

# sprawdź ile razy dany element występuje na liście
count = 0
for element in randomList:
    if(element == find):
        count += 1
print("Element %i występuje w liście %i razy" % (find, count))




