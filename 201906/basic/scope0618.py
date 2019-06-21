s = "123"


def fun():
    print(s)


fun()


def func():
    global s
    s = 10


func()
print(s)