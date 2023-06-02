from datetime import datetime

SAT = 5
SUN = 6

WEEKEND = (SAT, SUN)


def is_holiday(date: datetime):
    return date.weekday() in WEEKEND
