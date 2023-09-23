# map and filter func
a = map(lambda s: s.lower() if s in 'aeiou' else s.upper(), "shunate")

print(tuple(a))
print(a)
# map returs an object e.g. list, tuple, etc
numbers = [1, 2, 3, 4, 5]
squared = map(lambda num: num**2, numbers)

print(list(squared))

numbers = [2, 4, 5, 6, 9, 10]
even = filter(lambda num: num % 2 == 0, numbers)
print(list(even))
print(even)
