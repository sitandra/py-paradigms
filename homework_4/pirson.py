import random

def average(array):
    s = 0
    for i in array:
        s+=i
    return s/len(array)

def calcPirson(x, y):
    denominatorX = 0
    denominatorY = 0
    avX = average(x)
    avY = average(y)
    numerator = lambda xi,yi: (xi - avX) * (yi - avY)
    denominatorX = lambda xi: (xi - avX) ** 2
    denominatorY = lambda yi: (yi - avY) ** 2
    return sum(list(map(numerator, x, y))) / ((sum(list(map(denominatorX, x))) ** 0.5) * (sum(list(map(denominatorY, y))) ** 0.5))


x = []
y = []
for i in range(10):
    x.append(random.choice(range(-10,11)))
    y.append(random.choice(range(-10,11)))
print(x)
print(y)
print(calcPirson(x,y))


