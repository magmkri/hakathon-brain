import datetime

def checkIfWeekend(time):
    weekno = time.weekday()
    if weekno >= 5:
        return True
    else:
        return False
