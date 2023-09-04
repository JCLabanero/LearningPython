max_num = int(input("Enter a number: "))

current_num = 1
row = 1

while current_num <= max_num:
    for _ in range(row):
        if current_num <= max_num:
            print(current_num, end="")
            current_num += 1
    print()
    row += 1
