def func(a, b, f):
    print f(a, b)
    return


func(1, 2, lambda x, y: x+y)
func(1, 2, lambda x, y: x-y)
func(1, 2, lambda x, y: x > y)
