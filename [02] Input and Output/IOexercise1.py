print("Hello, Python!")

# using formatted printing
print("%s is %d." % ("value", 3))
subject = "Python"
print("Let's study %s" % subject)
print("Let's study %s - %s" % ("404", subject))
pi = "PI"
value = 3.14159
print("The value of %s is %f." % (pi, value))
print("The value of %s is %.2f." % (pi, value))
print("The value of %s is %d." % (pi, value))

# using string format method
print("{} is {}.".format("value", 6))
print("{0} is {1}.".format("value", 6))  # can be indexed
print("{1} is {0}.".format("value", 6))  # can be indexed
print("{0} is {val}.".format("value", val=6))  # can be called with keyword

# F-Strings / formatted string
print(f"{'value'} is {6}.")
code = "IT 403 WMAD"
subject = "Python"
print(f"Let's study {code} - {subject}")
print(f"The value of {pi} is {value}.")
print(f"The value of {pi} is {value:.2f}.")  # balikan

fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print(f"Your name is {fnam} {lnam}.")

print("+" + 10 * "-" + "+")
print(("|"+" "*10+"|\n")*5, end="")
print("+"+10*"-"+"+")
