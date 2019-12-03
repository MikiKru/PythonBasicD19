def geometricSeries(n, a1 = 1, q = 2):
    cumSum = 0
    elements = []
    for i in range(0, n):
        cumSum += a1*pow(q,i)
        elements.append(a1*pow(q,i))
    return cumSum, elements

print(geometricSeries(4,a1=3, q=2))
