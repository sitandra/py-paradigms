import random

def average(array):
    s = 0
    for i in array:
        s+=i
    return s/len(array)

def calcPirson(x, y):
    numerator = 0
    denominatorX = 0
    denominatorY = 0
    avX = average(x)
    avY = average(y)
    for i in range(len(x)):
        numerator += (x[i] - avX) * (y[i] - avY)
        denominatorX += (x[i] - avX) ** 2
        denominatorY += (y[i] - avY) ** 2
    return numerator / ((denominatorX ** 0.5) * (denominatorY ** 0.5))

x = []
y = []
for i in range(10):
    x.append(random.choice(range(-10,11)))
    y.append(random.choice(range(-10,11)))
print(x)
print(y)
print(calcPirson(x,y))


