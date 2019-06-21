x = 0
try:
    a = 1 / x
except ZeroDivisionError:
    print(x)
finally:
    print("释放资源")
print("123")
