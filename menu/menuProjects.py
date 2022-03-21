from helper import c


def menu():
    c.prCyan("press 1 To Add product")
    c.prCyan("press 2 To Display all products")
    c.prCyan("press 3 To Display edit product")
    c.prCyan("press 4 To Display delete product")
    c.prCyan("press 5 To Display search product")
    c.prCyan("press 6 To Logout")

    num = input(" >> ")
    if num.isdigit() and int(num) in range(1, 7):
        return int(num)
    else:
        c.prRed("wrong choice")
        menu()
