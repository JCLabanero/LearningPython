# Text type: str
# Numeric type: int,float,complex
# Sequence type: list,tuple,range
# Mapping type: dict
# Set type: set, frozenset
# Boolean type: bool
# Binary type: bytes, bytearray, memoryview
x = "Hello world"  # string
print(type(x))
x = 20  # integer
print(type(x))
x = 20.5  # float
print(type(x))
x = 1j  # complex
print(type(x))
x = ["apple", "banana", "cheery"]  # list
print(type(x))
x = ("apple", "banana", "cherry")  # tuple
print(type(x))
x = range(6)  # range(start,stop,step)
print(type(x))
x = {"name": "John", "age": 36}  # object(other lang) dict
print(type(x))
x = {"apple", "banana", "cheery"}  # set
print(type(x))
x = frozenset({"apple", "cherry"})  # frozenset
print(type(x))
x = True  # bool
print(type(x))
x = b"Hello"  # bytes
print(type(x))
x = bytearray(5)  # bytearray
print(type(x))
x = memoryview(bytes(5))  # memoryview
print(type(x))
