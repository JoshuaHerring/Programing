from datetime import datetime, timedelta
today = datetime.now()
#time delta can be done with days, weeks, hours, months etc.
one_day = timedelta(days=1)
yesterday = (today-one_day)
print(today)
print('today is ' + str(today))
print('yesterday was ' +str(yesterday))
print('day '+str(today.day))
print('month '+str(today.month))
print('year ' +str(today.year))
# this ability to select day month and year can be done with minute hours and seconds as well
birthday = input('when is your birthday?')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
#you can learn what format to use for example the %d/%m/%Y in the striptime function description
#i still do not know how to do this
print('Your birthday is on '+str(birthday_date))