import math

print(math.pi)

a = -3
if a > 1:
    print(a)
else:
    print(a * 2)

s = 0
for i in range(101):
    s += i
print(s)

a = 1
r = 1.01
while True:
    a *= r
    if a > 2:
        break
print(a)
