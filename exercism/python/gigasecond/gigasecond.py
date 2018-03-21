import datetime

def add_gigasecond(birth_date):
    time = datetime.timedelta(0,1000000000)
    return birth_date + time
