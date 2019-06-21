a = "a"
b = "b"
print(a, b)
print(a + b)

arr = ["1", "2", "3"]
print(arr)
arr.append(123)
print(arr)
arr.insert(0, 321)
print(arr)
del arr[1:4]
print(arr)

print("----------------------")
str = "hello"
print(str)
print(list(str))

print("----------------------")
map = {"A": 1, "B": 2}
print(map)
map.update({"C":3})
print(map)


print("----------------------")
for k in map:
    print("{}->{}".format(k,map[k]))
print(map.values())
print(map.items())

print("----------------------")
print(2**3)
print(5//2)
print(False and True)
print(not True)
