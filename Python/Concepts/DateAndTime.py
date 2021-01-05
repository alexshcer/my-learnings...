import datetime ###maths with time got ezz :)x69
import pytz
#import maya #super useful
#https://github.com/timofurrer/maya to use maya
today= datetime.date.today()

birthday = datetime.date(2002,9,10)# creating date time object date time object
print(birthday) 
days_sinceBDAY = (today-birthday).days
print(days_sinceBDAY)

tdelta = datetime.timedelta(days=69)
print(today - tdelta)
print(today.month)
print(today.day)
print(today.weekday())

print(datetime.time(3,6,34))
#datetime.date (Y,M,D)
#datetime.time(h , m ,s ,ms)
#datetime.datetime(Y,M,D,h,m,s,ms)
hdelta = datetime.timedelta(hours=69)
print(datetime.datetime.now()+hdelta)

#timezone aware 
datetime_today = datetime.datetime.now(tz=pytz.UTC)
datetime_india = datetime_today.astimezone(pytz.timezone('Asia/kolkata'))
#Time zone link:: https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568
print(datetime_india)

for tz in  pytz.all_timezones:
    print(tz)
#starting formatting with dates
#2019-03-09 --> March 09,2019
print(datetime_today.strftime('%B %d,  %Y'))
datetime_formate =datetime_today.strftime('%B %d,  %Y') #strf here
#FORM Sept 20 ,2020 --> datetime(2019,3,9)
datetime_thing = datetime.datetime.strptime(datetime_formate,'%B %d,  %Y') # here strptime
print(repr(datetime_thing))
print(datetime_thing)
