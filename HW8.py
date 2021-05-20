from datetime import datetime, timedelta
from collections import defaultdict

DAYS = {
    0 : 'Monday',
    1 : 'Tuesday',
    2 : 'Wednesday',
    3 : 'Thursday',
    4 : 'Friday',
    5 : 'Saturday',
    6 : 'Sunday'
    }

def days (day):
    return DAYS[day]


def congratulate (users):
    congrat_now = defaultdict(list)
    present_day = datetime.now().date()
    differ = timedelta(days=5 - present_day.weekday())
    week_start = present_day + differ
    print(week_start)
    week_end = week_start + timedelta(days=7)
    print(week_end)


    for lst in users:
        new_el = lst['birthday'].date().replace(year=2021)

        if new_el>=week_start and new_el<=week_end:
            name = lst['name']
            day = new_el.weekday()
            w_day = days(day)
            if w_day == 'Sunday': w_day = 'Monday'
            congrat_now[w_day].append(name)
    print(congrat_now)




congratulate(({'name': 'Den', 'birthday': datetime(year=2000, month=5, day=16)}, {'name':'Kiril', 'birthday': datetime(year=1995, month=5, day=16)}, {'name':'Andrey', 'birthday': datetime(year=1994, month=5, day=22)},{'name':'Dmitriy', 'birthday': datetime(year=1993, month=5, day=23)}, {'name':'Anna', 'birthday': datetime(year=1990, month=5, day=18)}))