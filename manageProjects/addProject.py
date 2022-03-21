import random

from helper import c
from helper import days_between
from datetime import datetime
from manageProjects.handleFileProduct import appendToFileProjects as writeTo

projectForm = ["title",
               "Details",
               "Total target",
               "start time",
               "end time",
               ]
i = 0
dataInsert = {}
format = "%d-%m-%Y"
emailUser = ""


def addProject(email):
    c.prLightPurple(" ADD Project ")

    global i, dataInsert, emailUser
    i = 0
    dataInsert = {}
    emailUser = email
    dataInsert["id"] = random.randint(10000, 100000)
    getData()
    print(dataInsert)
    writeTo(dataInsert)
    return True





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
                return True
            else:
                c.prRed(f"Error data DD-MM-YYYY")
                return False

        elif which == "end time":
            if bool(datetime.strptime(value, format)):
                if days_between(dataInsert["start time"], value):
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


def getData():
    global i, dataInsert
    if i == 5:
        dataInsert["email"] = emailUser
        return True
    inputData = input(f"Please insert your {projectForm[i]} : ")
    if not inputData:
        c.prRed(f"Please insert value for {projectForm[i]}")
    else:
        res = validate(projectForm[i], inputData)
        if res:
            dataInsert[projectForm[i]] = inputData
            i += 1
    getData()
