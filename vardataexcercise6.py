global_greetings = "Hello Philippines!"
local_greetings = "Kamusta ka Pilipinas!"


def global_greeting():
    global global_greetings
    global_greetings = "Hello World!"


def local_greeting():
    local_greetings = "Hello Philippines!"


global_greeting()
local_greeting()

print("An example of global greetings is:", global_greetings)
print("An example of lcoal greetings in tagalog:", local_greetings)
