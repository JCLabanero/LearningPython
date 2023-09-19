# Text type: str
# Numeric type: int,float,complex
# Sequence type: list,tuple,range
# Mapping type: dict
# Set type: set, frozenset
# Boolean type: bool
# Binary type: bytes, bytearray, memoryview

# string
x = "Hello world"
print(type(x))

# integer
x = 20
print(type(x))

# float
x = 20.5
print(type(x))

# complex
x = 1j
print(type(x))

# list
x = ["apple", "banana", "cheery"]
print(type(x))

# tuple
x = ("apple", "banana", "cherry")
print(type(x))

# range(start,stop,step)
x = range(6)
print(type(x))

# object(other lang) dict
x = {"name": "John", "age": 36}
print(type(x))

# set
x = {"apple", "banana", "cheery"}
print(type(x))

# frozenset
x = frozenset({"apple", "cherry"})
print(type(x))

# bool
x = True
print(type(x))

# bytes
x = b"Hello"
print(type(x))

# bytearray
x = bytearray(5)
print(type(x))

# memoryview
x = memoryview(bytes(5))
print(type(x))
