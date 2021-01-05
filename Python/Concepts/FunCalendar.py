import calendar

print(calendar.weekheader(3))

def today():
    print(calendar.weekday(2020,9,17))
today()

print(calendar.month(2020,9))
print(calendar.monthcalendar(2020,9))
print(calendar.isleap(2020))
print(calendar.leapdays(2000,2018))
