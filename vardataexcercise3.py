student_id = 2019115313
student_fullname = "John Carlo Labanero"
student_age = 22
student_con_info = f"09201515123"
student_address = "CSJDM, Bulacan"
student_status = True
# print using F-string
print(f"Output#1\nID: {student_id}", f"Full name: {student_fullname}",
      f"Age: {student_age}", f"Contact: {student_con_info}", f"Address: {student_address}", f"Status: {student_status}", sep="\n")
# print using string.format
print("Output#2\nID: {}".format(student_id), "Name: {}\nAge: {}\nContact: {}\nAddress: {}\nStatus: {}".format(
    student_fullname, student_age, student_con_info, student_address, student_status), sep="\n")
# print using formatted with %
print("Output#3\nID: %d\nName: %s." % (student_id, student_fullname), "Age: %d" %
      student_age, "Contact: %s\nAddress: %s\nStatus: " % (student_con_info, student_address), sep="\n", flush=True)
