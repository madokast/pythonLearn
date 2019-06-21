import math

r = 1.0

for i in range(3, 100):
    a = 360.0 / float(i)
    d = 2 * math.sin(a / 2.0 / 180 * math.pi)
    length = d * i
    pi = length / 2.0
    print(pi)
