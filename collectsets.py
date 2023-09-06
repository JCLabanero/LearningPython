#sets unordered collection, does not record element position and order of insertion
list = []
tuples = ()
dictionaries = {#dupes keys gives warning
    "key":"value"
}
sets = {'violet', 'red', 'black', 'brown', 'blond', 'red', 'black'} 
#dupes does not allow, auto delete if dupe insert
print(sets)
for hair in sets:
    print(hair)

sets.add('black')
print(sets)
sets.add('sugar')
print(sets)
sets.update(['black','demon'])
print(sets)
sets.pop()
print(sets)
sets.remove('blond')
print(sets)
sets.discard('blond')
sets.discard('red')
print(sets)
print(len(sets))