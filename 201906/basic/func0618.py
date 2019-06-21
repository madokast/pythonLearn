def fun():
    print("hello")


def sqr(a):
    return a * a


fun()
print(str(12))

f = lambda x: x * x
print(f(2))


def f(*a):
    for i in a:
        print(i)
    print(a)


# (1, 2, 'b', 'a')

f(1, 2, "b", "a")
