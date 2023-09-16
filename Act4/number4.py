name = input("Enter a text: ")

# for letter in name:
#     if name[0]==letter:
#         print(name)
#         continue
#     print(letter+(name.count-2)*" "+letter[])
name = name.replace(" ","")
for number in range(len(name)):
    if number == 0:
        print(name)
        continue
    if number == len(name)-1:
        print(name[::-1])
        break
    print(name[number:number+1]+" "*(len(name)-2)+name[len(name)-(number+1)])