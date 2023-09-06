#dict are unordered, changeable, and indexed. Dict have keys and values
#key value pair
info = {
    "name":"Paul",
    "age":28,
    "course": "DIT"
}
print(info["name"])#access by key
print(info.get("course"))
info["name"] = "Carlo"
print(info["name"])
info["status"] = "singul"
print(info)
info.pop("course")
print(info)
info.popitem()
print(info)
print(len(info))

