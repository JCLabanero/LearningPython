# try:
#     args = int(input("Enter low-high"))
#     print(args)
# except ValueError as val:
#     print(val)
# value min max

def read_int(prompt, min, max):
    isContinue = True
    while isContinue:
        try:
            enter = int(input(prompt))
            assert enter >= min and enter <= max
            break
        except ValueError:
            print("Error: wrong input")
        except AssertionError:
            print(
                f"Error: the value is not within the permitted range ({min}..{max})")
    return enter


v = read_int("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", v)
