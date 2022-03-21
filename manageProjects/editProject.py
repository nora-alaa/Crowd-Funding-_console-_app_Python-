from helper import c
from helper import days_between
from manageProjects.handleFileProduct import checkSameUserAndExistId
from manageProjects.handleFileProduct import editProject as editProjectToDB
from datetime import datetime

id = 0
oldData = {}
mappingNumToWord = ["title", "Details", "Total target", "start time", "end time"]
format = "%d-%m-%Y"


def editProject(email):
    c.prLightPurple(" Edit project ")
    global id, oldData
    c.prPurple("Insert ID To Modify")
    id = input(" >> ")
    if id and id.isdigit():
        res = checkSameUserAndExistId(id, email)
        if not res["status"]:
            c.prRed(res["message"])
            return False
        else:
            oldData = res["message"]
            print(type(oldData))
            editProcess()
            return True
    else:
        c.prPurple("Please insert number")
        editProject()


def editProcess():
    num = menu()
    if num == 6:
        editProjectToDB(oldData)
        return True
    key = mappingNumToWord[num-1]
    c.prPurple(f"Insert new {key} To Modify")
    newValue = input(" >> ")
    if validate(key,newValue):
        oldData[key] = newValue
    editProcess()


def validate(which, value):
    try:
        if which == "Total target":
            if value.isdigit():
                return True
            else:
                c.prRed(f"Must be a number")
                return False

        elif which == "start time":
            if bool(datetime.strptime(value, format)):
                if days_between(value,oldData["end time"]):
                    return True
                else:
                    c.prRed(f"start date must be before end date")
                    return False
            else:
                c.prRed(f"Error data DD-MM-YYYY")
                return False

        elif which == "end time":
            if bool(datetime.strptime(value, format)):
                if days_between(oldData["start time"], value):
                    return True
                else:
                    c.prRed(f"end date must be after start date")
                    return False
            else:
                c.prRed(f"Error data DD-MM-YYYY")
                return False

        else:
            return True
    except:
        c.prRed("Format Error")



def menu():
    c.prLightPurple(f"project ID : {id}")
    c.prCyan("press 1 To Edit title")
    c.prCyan("press 2 To Edit Details")
    c.prCyan("press 3 To Edit Total target")
    c.prCyan("press 4 To Edit start time")
    c.prCyan("press 5 To Edit end time")
    c.prCyan("press 6 To Edit Finish")

    num = input(" >> ")
    if num.isdigit() and int(num) in range(1, 7):
        return int(num)
    else:
        c.prRed("wrong choice")
        menu()
