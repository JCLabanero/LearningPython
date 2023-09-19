# arg+kwargs
def computeAverage(name, **grades):
    sum = 0
    for v in grades.values():
        sum += v
    print(
        f"\n{name}'s grades ({', '.join([f'{k}={v}' for k,v in grades.items()])}) and the average is {sum/len(grades):.2f}")


computeAverage(
    input("Enter name: "),
    Math=int(input("Math grade: ")),
    Science=int(input("Science grade: ")),
    English=int(input("English grade: ")),
    Music=int(input("Music grade: ")),
    Arts=int(input("Arts grade: ")),
)
