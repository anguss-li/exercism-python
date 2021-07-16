from calendar import day_name, monthrange, weekday
from datetime import date
from re import sub


class MeetupDayException(Exception):
    pass


def meetup(year: int, month: int, week: str, day_of_week: str) -> date:
    if week == 'teenth':
        week = range(13, 20)
    elif week == 'last':
        last_day = monthrange(year, month)[1]
        week = range(last_day, last_day-7, -1)
    else:
        week_no = (int(sub(r'[a-z]+', '', week))-1)*7 + 1
        week = range(0 + week_no, 8 + week_no)
    try:
        for day in week:
            if day_name[weekday(year, month, day)] == day_of_week:
                return date(year, month, day)
    except ValueError:
        raise MeetupDayException("Meetup day date cannot be found")
