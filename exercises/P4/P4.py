a = 1
b = 2.4
c = "w1"
print(a,b,c)
print(a,b,c, sep=' | ')

a = 2.1
b = "abc"
c = 0
print(a,b,c)

b = c
a = 13
print(a,b,c)

del(a)
del(c)
# c = c + 31.3      -> c is not defined
# print( c )