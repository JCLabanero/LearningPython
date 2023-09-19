# kwargs
# **kwargs - keyword arguments
# arguments are passed as dictionary using **kwargs
def info(**data):
    return f"Hello {data['fname']} {data['lname']}!"


print(info(fname="Jhaycee", lname="Swing"))
print(info(fname="Jan Carlo", lname="Salorio"))
