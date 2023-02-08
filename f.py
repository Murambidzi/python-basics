def name():
    print("Hello World")

def student_details(studentid, name, surname, programme):
    d = "these are student details" + studentid
    d += name

    d += surname

    d += programme
    return d