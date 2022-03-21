from manageProjects.handleFileProduct import getAllProjects
from prettytable import PrettyTable
from helper import c


def displayProjects():
    c.prLightPurple(" All projects ")
    allData = getAllProjects()
    t = PrettyTable(["id", "title", "Details", "Total target", "start time", "end time", 'By'])
    for p in allData:
        project = eval(p)
        t.add_row(project.values())
    print(t)
