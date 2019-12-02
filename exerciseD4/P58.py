def fibonacciSeries(n):
    fibo = [0, 1]
    if(n == 0):
        return [0], 0, 0
    if(n == 1):
        return fibo, 1, 1
    cumSum = 1
    for i in range(2,n):
        fibo.append(fibo[i-1] + fibo[i-2])
        cumSum += fibo[i]
    return fibo, fibo[len(fibo)-1],cumSum

print(fibonacciSeries(5))