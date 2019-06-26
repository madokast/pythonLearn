import numpy as np

def fun(**kwargs):
    return kwargs


print(fun(a=1, b=2))
A = fun(a=1, b=2)
print(A.__len__())
for t in A.keys():
    print(t)
    print(A.get(t))


for i in range(4):
    print(i)

x=np.array([1,2,3])
print(x)
print(x[1:3])
