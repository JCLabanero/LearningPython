x = y = 5
print(1 if x % y == 0 else 0, end="")
x += 5
print(x % y if x % y != 0 else 0, end="")
x, y = x, y
print(1 if x % y == 0 else 0, end="")
x, y = 1, x
print(x % y if x % y != 0 else 0, end="")
x += 5
print(1 if x % y == 0 else 0, end="")
