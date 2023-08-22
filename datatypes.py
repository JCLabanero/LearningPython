x = "Hello world"
print(type(x))  # string
x = 20
print(type(x))  # integer
x = 20.5
print(type(x))  # float
x = 1j
print(type(x))  # complex
x = ["apple", "banana", "cheery"]
print(type(x))  # list
x = ("apple", "banana", "cherry")
print(type(x))  # tuple
x = range(6)
print(type(x))  # range
x = {"name": "John", "age": 36}
print(type(x))  # object(other lang) dict
x = {"apple", "banana", "cheery"}
print(type(x))  # set
x = frozenset({"apple", "cherry"})
print(type(x))  # frozenset
x = True
print(type(x))  # bool
x = b"Hello"
print(type(x))
x = bytearray(5)
print(type(x))
x = memoryview(bytes(5))
print(type(x))

# Text type: str
# Numeric type: int,float,complex
# Sequence type: list,tuple,range
# Mapping type: dict
# Set type: set, frozenset
# Boolean type: bool
# Binary type: bytes, bytearray, memoryview
