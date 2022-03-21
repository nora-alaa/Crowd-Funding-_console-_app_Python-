from helper import c


def checkSameUserAndExistId(id, email):
    allData = getAllProjects()
    for project in allData:
        dataProject = eval(project)
        if dataProject["id"] == int(id):
            if dataProject["email"] == email:
                return {'status': True, 'message': dataProject}
            else:
                return {'status': False, 'message': "Can't, you don't have permission"}
    return {'status': False, 'message': "ID " + id + " doesn't exist"}


def appendToFileProjects(info):
    try:
        with open('projects.txt', 'a') as project:
            project.write(f"{info}\n")
    except:
        c.prRed("Can't open file")


def getAllProjects():
    allData = []
    try:
        with open('projects.txt', 'r') as project:
            allData = project.readlines()
        return allData
    except:
        c.prRed("Can't open file")
        return allData


def editProject(newData):
    try:
        allData = getAllProjects()

        with open('projects.txt', 'w') as project:
            for p in allData:
                data = eval(p)
                if data["id"] == newData["id"]:
                    project.write(f"{newData}\n")
                else:
                    project.write(f"{p}")

    except:
        c.prRed("Can't open file")


def deleteProcess(id):
    try:
        allData = getAllProjects()
        with open('projects.txt', 'w') as project:
            for p in allData:
                data = eval(p)
                if data["id"] == id:
                    pass
                else:
                    project.write(f"{p}")

    except:
        c.prRed("Can't open file")


