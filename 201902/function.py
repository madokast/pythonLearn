a = 1


def fun():
    global a
    print a
    a = 100
    print a
    return


fun()
