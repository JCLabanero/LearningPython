# sets unordered collection, does not record element position and order of insertion
list = []
tuples = ()
dictionaries = {  # dupes keys gives warning
    "key": "value"
}
sets = {'violet', 'red', 'black', 'brown', 'blond', 'red', 'black'}
# dupes does not allow, auto delete if dupe insert
print(sets)
for hair in sets:
    print(hair)

sets.add('black')
print(sets)
sets.add('sugar')
print(sets)
sets.update(['black', 'demon'])
print(sets)
sets.pop()
print(sets)
sets.remove('blond')
# sets.remove('blond')  # gives warning
print(sets)
sets.discard('blond')
sets.discard('blond')  # does not give warning
sets.discard('red')
print(sets)
print(len(sets))
the = "The quick brown fox jumps over the lazy dog."
the = set(the)
print(the)
why = []
why.extend(the)
why.sort(reverse=True)
# why =
print(why)
