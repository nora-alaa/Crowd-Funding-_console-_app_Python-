from manageUsers import register
from manageUsers import login
from helper import c
from menu import menuUser
from menu import menuProjects
from manageProjects import addProject
from manageProjects import displayProjects
from manageProjects import editProject
from manageProjects import deleteProject
from manageProjects import searchProjects


isLogin = False
emailUser = ""
choice = -1
choiceMenuProjects = -1


def start():
    global choice
    choice = menuUser()
    resChoice()


def startProjects():
    global choiceMenuProjects
    choiceMenuProjects = menuProjects()
    resChoiceProjects()


def resChoice():
    global isLogin, emailUser
    if choice == 1:
        if register():
            c.prGreen("Done add user successfully")
        else:
            c.prRed("Email not unique")
        start()
    elif choice == 3:
        return

    else:
        res = login()
        if res["status"]:
            isLogin = True
            emailUser = res["email"]
            c.prGreen("Done login")
            startProjects()
        else:
            c.prRed("Wrong password or email")
            start()


def resChoiceProjects():
    global isLogin, emailUser, choice, choiceMenuProjects
    if choiceMenuProjects == 1:
        if addProject(emailUser):
            c.prGreen("Done add projects successfully")
        startProjects()
    elif choiceMenuProjects == 2:
        displayProjects()
        startProjects()

    elif choiceMenuProjects == 3:
        if editProject(emailUser):
            c.prGreen("Edit Done successfully")
        startProjects()

    elif choiceMenuProjects == 4:
        if deleteProject(emailUser):
            c.prGreen("Delete Done successfully")
        startProjects()

    elif choiceMenuProjects == 5:
        searchProjects()
        startProjects()

    elif choiceMenuProjects == 6:
        isLogin = False
        emailUser = ""
        choice = -1
        choiceMenuProjects = -1
        start()


start()
