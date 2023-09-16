nums = [
["####","   #","####","####","#  #","####","####","####","####","####"],
["#  #","   #","   #","   #","#  #","#   ","#   ","   #","#  #","#  #"],
["#  #","   #","####","####","####","####","####","   #","####","####"],
["#  #","   #","#   ","   #","   #","   #","#  #","   #","#  #","   #"],
["####","   #","####","####","   #","####","####","   #","####","####"],
]
inputing = input("Enter numbers: ")
if inputing.isnumeric():
    for count in range(5):
        for letter in inputing:
            print(nums[count][int(letter)],end=" ")
        print()
else:
    print("Invalid")
# try:
# except TypeError as err:
#     print(err)asdfasd