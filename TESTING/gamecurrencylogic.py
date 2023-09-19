money = 1_000.0
con = True
while con:
    userInput = input("[0]Exit [1]Withraw [2]Deposit\nEnter your choice: ")
    if not userInput.isdigit:
        continue
    convertedInpu = int(userInput)
    if convertedInpu not in range(3):
        print("Not within the choice")
    if convertedInpu == 0:
        print("Exited")
        con = False
    elif convertedInpu == 1:

        pass
    elif convertedInpu == 2:
        pass
