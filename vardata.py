name = "John Carlo"
age = 35
print(f"There once was a man named {name},", f"he was {age} years old.",
      f"He really liked the name {name}", f"but didn't like being {age}.", sep="\n")
# dynamically type variable
print(type(name))
name = 3.9
print(name, type(name))
name = "JC"
age = 99.999
print(f"There once was a man named {name},", f"he was {age} years old.",
      f"He really liked the {name}", f"but didn't like being {age}.", sep="\n")
