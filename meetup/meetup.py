from calendar import day_name, monthrange, weekday
from datetime import date


class MeetupDayException(Exception):
    pass


def meetup(year: int, month: int, week: str, day_of_week: str) -> date:
    if week == 'teenth':
        search_range = range(13, 20)
    elif week == 'last':
        last_day = monthrange(year, month)[1]
        search_range = range(last_day, last_day-7, -1)
    else:
        week_num = int(week[0])*7 - 6
        search_range = range(0 + week_num, 8 + week_num)
    try:
        for day in search_range:
            if day_name[weekday(year, month, day)] == day_of_week:
                return date(year, month, day)
    except ValueError:
        raise MeetupDayException("Meetup day date cannot be found")
