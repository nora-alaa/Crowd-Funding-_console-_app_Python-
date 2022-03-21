from datetime import datetime

format = "%d-%m-%Y"


def days_between(d1, d2):
    d1 = datetime.strptime(d1, format)
    d2 = datetime.strptime(d2, format)
    return (d2 - d1).days > 0
