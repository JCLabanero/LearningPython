def withraw(value):
    global money
    if money <= 0:
        print("0 balance")
    elif value > money:
        print("balance is not enough")
    elif value <= money:
        money -= value
        print("successfully withrawn %.2f" % value)
        # print(f"successfully withrawn {value:.2f}")
        # print("successfully withrawn {}".format(value))
    else:
        print("error!")


def deposit(value):
    global money
    if (value > 0):
        money += value
        print("deposit successfully")
    else:
        print("deposit failed!")


PIN = "0412"
money = 10.0
isContinue = True
pin = ""
while (pin != PIN):
    pin = input("Enter 4 digit code: ")
    if pin != PIN:
        print("wrong PIN")

while (isContinue):
    print("[1] Withraw", "[2] Deposit",
          "[3] Check Balance", "[0] Exit", sep=", ")
    userOp = input("Enter your option: ")
    if userOp == "1":
        userWithrawValue = float(input("Input amount: "))
        withraw(userWithrawValue)
    elif userOp == "2":
        userDepositValue = float(input("Input amount: "))
        deposit(userDepositValue)
    elif userOp == "3":
        print("You current balance is: {}".format(money))
    elif userOp == "0":
        isContinue = False
        print("Thank you! come again next time.")
    else:
        print("Input failed")
print("success!")
