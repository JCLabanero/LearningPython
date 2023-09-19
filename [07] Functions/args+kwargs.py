# args+kwargs
def subjectsEnrolled(*subjects, **description):
    print(f"Name: {description['name']}")
    i = 1
    for subject in subjects:
        print(f"Subject {i}: {subject}")
        i += 1
    for k, v in description.items():
        print(f"{k} => {v}")


subjectsEnrolled(
    input("Subject 1: "),
    input("Subject 2: "),
    input("Subject 3: "),
    name=input("Enter Name:  "),
    IT402=input("Enter Description for IT 402: "),
    IT403=input("Enter Description for IT 403: "),
    IT404=input("Enter Description for IT 404: "),
)
