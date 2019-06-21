def fun(**kwargs):
    return kwargs


print(fun(a=1, b=2))
A = fun(a=1, b=2)
print(A.__len__())
for t in A.keys():
    print(t)
    print(A.get(t))
