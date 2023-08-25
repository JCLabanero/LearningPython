if (2+2 == 4):
    print("equal")
a = 33
b = 200
if b > a:
    print("b is greater than a")
if 2+3 == 5:
    print("Equal")
else:
    print("Not equal")
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")
if 2+3 < 5:
    print("Less than 5")
elif 2+3 > 5:
    print("greater than 5")
else:
    print("equal")
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

x = 1
y = 1.0
z = "1"
if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")
if 2+3 == 5:
    print("Equal")
print("Equal" if 2+2 == 4 else "Not Equal")
grade = 75
print("pass" if grade > 75 else "failed")
print("pass" if grade >= 75 else "failed")
