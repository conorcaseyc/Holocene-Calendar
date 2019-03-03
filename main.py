#Imports Dependences.
import datetime

#Fetches the Current Date and Time.
now = datetime.datetime.now()

#Adds a 0 to numbers below ten. This is for the month, day, hour, minute, and second time segments.
def check(time):
	if time < 10:
		return '0' + str(time)
	elif time > 10:
		return str(time)

#Creates time segments in accordance with the Holocene Calendar.
year = now.year + 10000
month = check(now.month)
day = check(now.day)
hour = check(now.hour)
minute = check(now.minute)
second = check(now.second)

#Records the date and time into two separate variables 
time = str(hour) + ':' + str(minute) + ':' + str(second)
#ISO 8601
iso_date = str(year) + '-' + str(month) + '-' + str(day)
#DD/MM/YYYY (Normally)
dmy_date = str(day) + '-' + str(month) + '-' + str(year)
#MM/DD/YYYY (Normally)
mdy_date = str(month) + '-' + str(day) + '-' + str(year)

#Prints the date and time.
print('It is currently:', iso_date, time, '(ISO 8601)')
print('It is currently:', dmy_date, time, '(Typically DD/MM/YYY)')
print('It is currently:', mdy_date, time, '(Typically MM/DD/YYY)')