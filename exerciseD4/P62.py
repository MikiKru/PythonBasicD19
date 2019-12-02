def nonDefinedParameters(*elements):        # parametr gwiazdka -> przyjmuje dowolną liczbę argumentów
    sum = 0
    for elem in elements:
        sum += elem
    return sum/len(elements)

print(nonDefinedParameters(1))
print(nonDefinedParameters(5,4,6))
print(nonDefinedParameters(2,2,2,2))