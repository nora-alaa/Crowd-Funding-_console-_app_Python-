from helper import c
from manageProjects.handleFileProduct import checkSameUserAndExistId
from manageProjects.handleFileProduct import deleteProcess

def deleteProject(email):
    c.prLightPurple(" Delete project ")
    global id
    c.prPurple("Insert ID To Delete")
    id = input(" >> ")
    if id and id.isdigit():
        res = checkSameUserAndExistId(id, email)
        if not res["status"]:
            c.prRed(res["message"])
            return False
        else:
            oldData = res["message"]
            deleteProcess(oldData["id"])
            return True
    else:
        c.prPurple("Please insert number")
        deleteProject()




