char = input("Enter a character: ")
num = int(input("Enter a number: "))


for i in range(1, num+1):
    print((char+' ') * i)

for i in range(num - 1, 0, -1):
    print((char + ' ') * i)
