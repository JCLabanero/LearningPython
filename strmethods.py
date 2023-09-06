sample = " The quick brown fox jumps over the lazy dog. "
print(len(sample))
print(sample.upper())
print(sample.lower())
print(sample.capitalize())
print(sample.title())
sample = sample.title()
print(sample.swapcase())
# string boolean methods
number = "5"
letters = "aeiou"
alphanum = letters+number
alphanumspec = number + letters + "@"
print("This is numeric: \n", number.isnumeric(), sep="")
print(letters.isnumeric())
print("This is alphabet:\n", number.isalpha(), sep="")
print(letters.isalpha())
print("This is alphabet or numeric\n",
      number.isalnum(), sep="")  # alpha numeric
print(letters.isalnum())
print(alphanum.isalnum())
print(alphanumspec.isalnum())

str1 = "THIS IS A UPPER 123 !"
str2 = "this is a lower 123 !"
print("is lower?", str1.islower())
print("is lower?", str2.islower())

str1 = str1.title()
str2 = str2.capitalize()

print("is title?", str1.istitle())
print("is title?", str2.istitle())

str1 = "Alpha Beta Chad Delta Epsilon Giga"
str2 = "Beta Chad Delta Epsilon Giga Omega"

print("ends with?", str1.endswith("iga"))
print("ends with?", str2.endswith("iga"))
print("starts with?", str1.startswith("alpha".capitalize()))
print("starts with?", str2.startswith("alpha".capitalize()))

# joininh
tocombine = "John Carlo Pido Labanero"
print(" ".join(tocombine))
# print("_".replace(" ", "").join(str1))
print("_".join(str1))
names = ["Paul", "Gabriel", "Johnathan"]
print(", ".join(names))
# splitting
tosplit = tocombine
names = tosplit.split(" ")
print(names)

name = " ".join(names)
print(name)
print(name.find("Carlo"))  # returns -1 if none
names = "Paul,Gabriel,Johnathan"
print(names.replace(",", " "))


print(sample.strip())
print(sample.lstrip())
print(sample.rstrip())

# string ordinal method
print(ord('a'), ord(' '))
print(chr(97), chr(945))
print("abcdefgABCDEFG".index("A"))
