x, y = 20, 5
print(1 if x % y == 0 else 0, end="")
y += 5
print(x % y if x % y != 0 else 0, end="")
x, y = x, y
print(1 if x % y == 0 else 0, end="")
x, y = 10, x
print(x % y if x % y != 0 else 0, end="")
x += 10
print(1 if x % y == 0 else 0, end="")
