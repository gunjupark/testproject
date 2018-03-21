import calendar
import datetime

def meetup_day(year, month, day_of_the_week, which):
    x=0
    y=-1
    z=1
    cal = calendar.TextCalendar()
    list_c1 = cal.monthdayscalendar(year, month)
    list_c2 = cal.monthdatescalendar(year, month)
    wday = day_of_the_week[0:2]
    wdic = {'Mo':0,'Tu':1,'We':2,'Th':3,'Fr':4,'Sa':5,'Su':6}
    if which is 'teenth' :
        while list_c1[z][wdic.get(wday)]<13 : z+=1
    if list_c1[x][wdic.get(wday)] is 0 :
        x+=1
    if list_c1[-1][wdic.get(wday)] is 0:
        y=-2
    ndic = {'1st':x,'2nd':x+1, '3rd':x+2,'4th':x+3,'5th':x+4,'last':y,'teenth':z}
    return list_c2[ndic.get(which)][wdic.get(wday)]
