def bad_fun(n):
    raise ZeroDivisionError


try:
    bad_fun(0)
except (ArithmeticError, Exception):
    print("What happended? An error?")
print("THE END.")
