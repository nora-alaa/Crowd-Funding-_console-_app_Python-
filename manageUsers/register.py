from helper import c
import re
from manageUsers.handleFileUsers import appendToFileUsers as writeTo

registerForm = ["first name",
                "last name",
                "email",
                "password",
                "confirm password",
                "mobile phone"
                ]
i = 0
dataInsert = {}


def register():
    c.prLightPurple(" Registration Form ")

    global i, dataInsert
    i = 0
    dataInsert = {}
    getDataToRegister()
    if writeTo(dataInsert):
        return True
    else:
        return False


def validate(which, value):
    if which == "mobile phone":
        regexPhone = r'\b^01[0-2,5]\d{8}$\b'
        if re.fullmatch(regexPhone, value):
            return True
        else:
            c.prRed(f"Phone number must be 01[0,1,2,5]xxxxxxxxx")
            return False

    elif which == "email":
        regexEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regexEmail, value):
            return True
        else:
            c.prRed(f"email must be xxx@xxx.xxx")
            return False

    elif which == "confirm password":
        if value == dataInsert["password"]:
            return True
        else:
            c.prRed(f"confirm password doesn't match password")
            return False
    else:
        return True


def getDataToRegister():
    global i, dataInsert
    if i == 6:
        return True
    inputData = input(f"Please insert your {registerForm[i]} : ")
    if not inputData:
        c.prRed(f"Please insert value for {registerForm[i]}")
    else:
        res = validate(registerForm[i], inputData)
        if res:
            dataInsert[registerForm[i]] = inputData
            i += 1
    getDataToRegister()
