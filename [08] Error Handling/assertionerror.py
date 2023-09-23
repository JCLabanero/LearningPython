from math import tan, radians
angle = int(input('Enter integral angle in degress: '))
# We must be sure that angle != 90 + k * 1809
assert angle % 180 != 90
print(tan(radians(angle)))
