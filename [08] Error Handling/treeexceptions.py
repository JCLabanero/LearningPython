try:
    y = 1/0
except ZeroDivisionError:
    print("more concrete/leaves")
except ArithmeticError:
    print("before more general")
except Exception:
    print("much general")
except BaseException:
    print("root")
print("THE END.")
