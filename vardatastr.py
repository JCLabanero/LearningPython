print("This is a string\nAdded new line\tThis is a tab \"This is an escape \\ quotation mark\"")
# (\) this is an escape character
concat = "This is concat"
print(concat + " a string")
# string functions
string = "John Carlo"
print(string.lower())
print(string.upper())
print(string.isupper())
print(string.islower())
print(string.upper().isupper())
print(string.capitalize())
# count the characters
print(len(string))
# string count chars with index
print(string[5])
print(string[0:3])
print(string[5:7])
print(string.index("Car"))
print(string.index("C"))
# print(string.index("c")) error : case sensitive
print(string.replace("Carlo", "John"))
