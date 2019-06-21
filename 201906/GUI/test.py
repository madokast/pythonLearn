func = lambda: print(123) == None and print(321) == None

func()


class Text:
    @classmethod
    def fun(cls):
        print("aaa")

    def __init__(self):
        self.lfun = lambda: Text.fun()
        self.lfun()


test = Text()
