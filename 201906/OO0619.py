class Dog:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("destructor？"+self.name)

    def say(self):
        print(self.name, ": hello")


d = Dog("wawawa")
d2 = Dog("hahaha")
d.say()
d2.say()
