# normal arg + args
def subjectsEnrolled(name, *subjects):
    print(f"Name: {name}")
    i = 1
    for subject in subjects:
        print(f"Subject {i}: {subject}")
        i += 1


def subjectsEnrolled2(*subjects, name):
    print(f"Name: {name}")
    i = 1
    for subject in subjects:
        print(f"Subject {i}: {subject}")
        i += 1


subjectsEnrolled(
    input("Enter Name: "),
    input("Subject 1: "),
    input("Subject 2: "),
    input("Subject 3: "),
)
subjectsEnrolled2(
    input("Subject 1: "),
    input("Subject 2: "),
    input("Subject 3: "),
    name=input("Enter Name: "),
    # input("Enter Name: "), #would result into typeerror
)
