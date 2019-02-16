print("123" if True else "abc")
#123

print(1+1 if False else 2+2)
#4

#and or not


try:
    1/0
except:
    print("!!")
else:
    print("??")
finally:
    print("close all")
#!!
#close all
