def factorial(n):
    result = 1
    while(n > 1):
        result *= n     # result = result * n
        n -= 1          # n = n -1
    return result
def factorialRec(n):
    if(n == 2):
        return n
    return n * factorial(n -1);


n = 5
print("%d!=%d" %(n,factorial(n)))
print("%d!=%d" %(n,factorialRec(n)))