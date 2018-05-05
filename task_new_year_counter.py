from datetime import datetime, time, timedelta
def counter():
    cur_day = datetime.today()
    new_year = datetime(cur_day.year + 1, 1, 1,)
    diff = new_year - cur_day
    days = diff.days
    secs = diff.seconds
    hours = secs // 3600
    minutes = (secs%3600) // 60
    summ = days_name(days)+ hours_name(hours) + minutes_name(minutes)
    summ_str = ' '.join(summ)
    print (summ_str)
    return summ_str


def days_name(days):
    if days == 0 or days % 10 == 0:
        return [str(days),'дней']
    elif days % 10 == 1 and days % 100 != 11:
        return [str(days),'день']
    elif days % 10 == 2 and days % 100 != 12:
        return [str(days),'дня']
    elif days % 10 == 3 and days % 100 != 13:
        return [str(days),'дня']
    elif days % 10 == 4 and days % 100 != 14:
        return [str(days), 'дня']
    else:
        return [str(days), 'дней']


def hours_name(hours):
    if hours % 10 == 1 and hours != 11:
        return [str(hours),'час']
    elif hours % 10 == 2 and hours != 12:
        return [str(hours),'часа']
    elif hours % 10 == 3 and hours != 13:
        return [str(hours),'часа']
    elif hours % 10 == 4 and hours != 14:
        return [str(hours),'часа']
    else:
        return [str(hours),'часов']

def minutes_name(minutes):
    if minutes % 10 == 1 and minutes != 11:
        return [str(minutes),'минута']
    elif minutes % 10 == 2 and minutes != 12:
        return [str(minutes),'минуты']
    elif minutes % 10 == 3 and minutes != 13:
        return [str(minutes),'минуты']
    elif minutes % 10 == 4 and minutes != 14:
        return [str(minutes),'минуты']
    else:
        return [str(minutes),'минут']


counter()
