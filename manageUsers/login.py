from manageUsers.handleFileUsers import findAtFile
from helper import c

i = 0
loginForm = ["email", "password"]
loginData = {}


def login():
    c.prLightPurple(" Login Form ")
    global i, loginData
    i = 0
    loginData = {}
    getDataToLogin()
    return checkLogin(loginData["email"], loginData["password"])


def getDataToLogin():
    global i
    if i == 2:
        return True
    inputData = input(f"Please insert  {loginForm[i]} : ")
    if not inputData:
        c.prRed(f"Please insert value for {loginForm[i]}")
    else:
        loginData[loginForm[i]] = inputData
        i += 1
    getDataToLogin()


def checkLogin(email, password):
    allData = findAtFile()
    res = {}
    for user in allData:
        dataUser = eval(user)
        if dataUser["email"] == email and dataUser["password"] == password:
            return {'status':True,'email':email}
    return {'status':False}
