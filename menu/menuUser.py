from helper import c


def menu():
    c.prCyan("press 1 To Register")
    c.prCyan("press 2 To Login")
    c.prCyan("press 3 To Exit")

    num = input(" >> ")
    if num.isdigit() and (int(num) == 1 or int(num) == 2 or int(num) == 3):
        return int(num)
    else:
        c.prRed("wrong choice")
        menu()
