from random import randint




def generateNRandomElements(n):
    elements = []
    for i in range(n):
        elements.append(randint(-1000,1000))
    print(elements)
    return elements
def getElementsSupportTreshold(n, treshold):
    elementsSupportTreshold = []
    cumSum = 0
    for elem in generateNRandomElements(n):
        if(elem > treshold):
            cumSum += elem
            elementsSupportTreshold.append(elem)
    return elementsSupportTreshold, cumSum

# print(generateNRandomElements(10))
print(getElementsSupportTreshold(10, 900))

from exerciseD4.P64 import returnColour

print(returnColour())



