def printwithforloop(typetoloop):
    for x in typetoloop:
        print(x)


typeStr = "JOHN"
typeList = ["apple", "banana", "cheery"]  # list
typeTuple = ("one", "two", "three")#immutable

typeRange = range(2)
typeObject = {"name": "John", "age": 36, "address": "csjdm"}
typeSet = {"apple", "banana", "cherry"}#unordered
typeFrozenSet = frozenset({"apple", "banana", "cherry"})#immutable and unordered sheesh
printwithforloop(typeStr)
printwithforloop(typeList)
printwithforloop(typeTuple)
# range is immutable (unchanging) range 3 output: 0 1 2
printwithforloop(typeRange)
printwithforloop(typeObject)
printwithforloop(typeSet)
printwithforloop(typeFrozenSet)

for x in range(3, 10):
    print(x)
for x in range(100, 130, 10):
    print(x)
# range(start,stop,step)
# for x, val in typeObject:
#     print(val)
