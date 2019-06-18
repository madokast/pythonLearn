myFile = open("./list0618.py", "r")
print(type(myFile))
str = myFile.readline()
while str!="":
    print(str[0:str.__len__()-1])
    str = myFile.readline()

myFile.close()

