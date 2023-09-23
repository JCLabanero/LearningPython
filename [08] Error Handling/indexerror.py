ilist = [1, 2, 3, 4, 5]
ix = 0
it = True
while it:
    try:
        print(ilist[ix])
        ix += 1
    except IndexError:
        it = False

print("Done")
