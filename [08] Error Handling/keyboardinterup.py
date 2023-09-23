from time import sleep
secondss = 0
while True:
    try:
        print(secondss)
        secondss += 1
        sleep(1)
    except KeyboardInterrupt:
        print("Don't do that!")
