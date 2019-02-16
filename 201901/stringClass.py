print("hello"[1]+",world")
#e,world

print("123456789"[::2])
#13579

print("123456789"[::-1])
#987654321

print("\"")
#"

print(".txt" in "text.txt")
#True

a = int("123") + 1
print(a)
#124

print("a b c d ".split(" "))
#['a', 'b', 'c', 'd', '']

print("this is a slot:{}, the second:{}, thrid:{}".format("1",2.2,333))
#this is a slot:1, the second:2.2, thrid:333

print("{:.5e}".format(1.0e-10/3))
#3.33333e-11