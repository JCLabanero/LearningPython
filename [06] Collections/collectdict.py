# dict are unordered, changeable, and indexed. Dict have keys and values
# key value pair
info = {
    "name": "Paul",
    "age": 28,
    "course": "DIT"
}
print(len(info))
print(info["name"])  # access by key
print(info["age"])
print(info.get("course"))  # access by get method
info["name"] = "Carlo"  # update
print(info["name"])
info["status"] = "singul"  # update
print(info)
info.pop("course")  # remove
print(info)
info.popitem()  # remove last
print(info)
print(len(info))
dictionaries = {  # dupes keys gives warning
    "key": "value"
}
