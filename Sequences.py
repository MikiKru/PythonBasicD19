sentence = "Ala ma kota, a kot ma Ale."
# oczyść zdanie ze znaków interpunkcyjnych
sentence = sentence.replace(",","")
sentence = sentence.replace(".","")
print(sentence)
# zapisz wsyztkie słowa w zdaniu w liście words
words = sentence.split(" ")
print(words)

# listy
params = []
row = [1, "Adam", "Nowak", "2000-01-01", True, 5500.]

# dodawanie parametrów do parms
params.append(12.5)
params.append(11.5)
params.append(9.4)
# wypisanie elementów listy
print(params)
print(row)
# zmiana pensji w liście row
row[5] = 6000.
print(row)
print(row[1:3])
#  odczyt elementów z krokiem 2
print(row[0:5:2])
print(row[1:])
print(row[:3])
# odwrotna kolejność
print(row[::-1])
# Powielanie list
row = row * 2
print(row)
# row *= 0        # row = row * 0
print(row)
# długośc listy
print(len(row))
# row[1] = "abc"
row[6:] = [2, "Jan","Kowalski","2011-02-12",False, 10000]
print(row)

a = ["a",1, True]
b = ["a", "xyz", 15.3]
print(b[1] == a[0:2])

# operator przynależności
print("Kowalski" in row)
print("Kowalski" not in row)


name = "Michał"
# name[3] = 'k'         NIEZMIENNY
# konwersja na listę
name = list(name)       # EDYTOWALNY
name[3] = 'k'
print(name)
string = ""
for v in name:
    string += str(v);
print(string)           # NIEZMIENNY
# string[2] = 'a'

print(name)
name = str(name)
name = name.replace("'","")
name = name.replace(", ","")
name = name.replace("]","")
name = name.replace("[","")
print(name)

numbers = [1,2,3,4,5]
numbers.remove(numbers[3])      # usuwanie po wartości bez zwracania
print(numbers)
deleted = numbers.pop(2)        # usuwanie po indeksie ze zwracaniem wartości
print(numbers)
print(deleted)

# sprawdź czy dwa napisy są palindromami
# sprawdź czy dwie liczby są lustrzane
# I SPOSÓB
text = "kajak"
print(text[ : ] == text[ : :-1])
# II SPOSÓB
text = list(text)
textRev = text
textRev.reverse()
print(text == textRev)

# sortowanie
nums = [1.1, 2.1, 0.15, 15., 1., 4., 1]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
names = ["Ala","Ola","Ela"]
names.sort()
print(names)

kik =   [
            ["_","_","_"],
            ["_","_","_","_"],
            ["_","_","_","_","_"]
        ]
print(kik)
print("lista zewnętrzna", len(kik))
print("pierwszy wiersz", len(kik[0]))
print("drugi wiersz", len(kik[1]))
print("trzeci wiersz", len(kik[2]))
kik[2][3] = "X"
print(kik)
kik[1][1:3] = ["O","O"]
print(kik)

kik.append(["*","*","*"])
print(kik)

kik.insert(0,["*","*","*"])
kik = [["^","^","^"]] + kik
print(kik)
print(len(kik))


tupleType = (1,2,3,4,5)
# tupleType[1] = 55   # krotka jest typem niezmiennym
print(tupleType)
a = [1,2]
multiDimTuple = (a, [3,4], [5,6])
# multiDimTuple[0] = 1
multiDimTuple[0].append('X')
multiDimTuple[0][0] = 2
print(multiDimTuple)
a.append(5)
print(multiDimTuple)
print(id(a))
print(id(multiDimTuple[0]))

a1 = 1
a2 = a1
a1 = 2
print(id(a1), id(a2), a1, a2)


#Słowniki
products = {}
# dodanie nowego produktu
products["0x111"] = "Pamięć RAM 8GB"
products["0x112"] = "Pamięć RAM 16GB"
products["0x222"] = [1,"PC", "Intel i5 8gen", 700]
# modyfikacja pamięci ram
products["0x112"] += " NEW"
products[None] = "xxx"
print(products[None])
print(products)
print(products.keys())
print(products.values())

# Zbiory
A = set([1,2,3,4,5,6])
B = set([4,5,6,7,8])

print("suma", A | B)
print("część wspólna", A & B)
print("różnica A-B", A - B)
print("różnica B-A", B - A)
print("różnica symetryczna", B ^ A) # suma - część wspólna

# Dla zdania wprowadzonego przez użytkownika sprawdź ile jest unikatowych słów
# zakładamy że w zdaniu nie wysępują znaki interpunkcyjne
# sentence = input("wpisz zdanie").upper()
# words = sentence.split(" ")
# uniqueWords = set(words)
# print("Ilość unikatowych słów: ", len(uniqueWords))
# print("Ilość powtórzeń słów: ", len(words) - len(uniqueWords))

S = set([1,2,3])
L = ['a','a','A']
D = {'a' : 11, 'b' : 11, 'c' : 1}
print(S)
print(list(S))
print(set(L))
print(D)
print(set(D))
print(set(D.keys()))
print(set(D.values()))










