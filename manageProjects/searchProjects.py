from helper import c
from manageProjects.handleFileProduct import getAllProjects
from prettytable import PrettyTable
from datetime import datetime
from helper import days_between

format = "%d-%m-%Y"
date = "1-1-1111"


def searchProjects():
    try:
        c.prLightPurple(" Search projects ")
        global date
        c.prPurple("Insert Date To Search")
        date = input(" >> ")
        if date and bool(datetime.strptime(date, format)):
            displayCertainProjects(date)

        else:
            c.prPurple("Please insert date format DD-MM-YYYY")
            searchProjects()
    except:
        c.prRed("Format Error")
        searchProjects()


def displayCertainProjects(date):
    c.prLightPurple(f" All projects which start-date after and end-date before {date}  ")
    allData = getAllProjects()
    t = PrettyTable(["id", "title", "Details", "Total target", "start time", "end time", 'By'])
    for p in allData:
        project = eval(p)
        if days_between(project["start time"], date) and days_between(date, project["end time"]):
            t.add_row(project.values())
    print(t)
