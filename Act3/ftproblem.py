while True:
    starting_year = int(input("Enter starting year: "))
    ending_year = int(input("Enter ending year: "))

    if starting_year >= ending_year:
        print("Starting year must be set before the ending year!")
        continue
    else:
        break


days_count = 0
for year in range(starting_year, ending_year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_count += 366
    else:
        days_count += 365

print(
    f"January 1, {ending_year} was {days_count} days after January 1, {starting_year}.")
