from math import sqrt


def calculateDistance3D(p1, p2):
    return sqrt(pow(p2[0] - p1[0],2) + pow(p2[1] - p1[1],2) + pow(p2[2] - p1[2],2))

p1 = [-2,-1,1]
p2 = [-2,1,1]
print(calculateDistance3D(p2, p1))