from helper import c


def uniqueEmail(email):
    allData = findAtFile()
    for user in allData:
        dataUser = eval(user)
        if dataUser["email"] == email:
            return False
    return True


def appendToFileUsers(info):
    try:
        if uniqueEmail(info["email"]):
            with open('users.txt', 'a') as users:
                users.write(f"{info}\n")
            return True
        else:
            return False
    except:
        c.prRed("Can't open file")


def findAtFile():
    allData = []
    try:
        with open('users.txt', 'r') as users:
            allData = users.readlines()
        return allData
    except:
        c.prRed("Can't open file")
        return allData
