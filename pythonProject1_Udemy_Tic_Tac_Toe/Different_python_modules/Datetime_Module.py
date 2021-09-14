from datetime import time
my_time = time(6, 35, 20, 234)
print(my_time)
print(my_time.max)
print(my_time.replace(minute=40))
print(my_time.hour)
# write the time in HH-MM-SS-MS format
print(my_time.strftime("%H-%M-%S-%f"))
t1 = time(14, 39)
print(t1.strftime("%H:%M:%S"))

#timestamp =time.time()
#print("The timestamp in sec: ", timestamp)
#print(time.gmtime(timestamp))
# print(time.localtime(timestamp))

print("-------------------------------------")


from datetime import date
my_date = date(2021, 6, 14)
print(my_date)
print(my_date.weekday())  # returns the day of a week like Mon, then returns 0, Tues, then 1
print(my_date.replace(2020))
print(my_date.fromisoformat("2020-06-14")) # checks for ISO 6801 standard
# write the date in YYYY/fullmonth/day
print(my_date.strftime("%Y/%B/%d %a"))


today = date.today()
print(today)
print(today.ctime())
# Create a timedelta
d1 = date(2021, 1, 10)
d2 = date(2021, 2, 14)
print(d2-d1)
print("--------------------------------")

import datetime
# Create a datetime object
#dt = datetime.today()
#print(dt)
#dt1 = datetime.now()
#print(dt1)
my_date_time1 = datetime.datetime(2021, 3, 11, 23, 23, 30, 34)
print(my_date_time1)
print(my_date_time1.strftime("%Y/%b/%d %H:%M:%S:%f"))
my_date_time2 = datetime.datetime(2021, 3, 10, 0, 20, 10)
# my_date_time2 = my_date_time2.replace(day=15)
print(my_date_time2)
print(abs(my_date_time2 - my_date_time1))
print(my_date_time1 - my_date_time2)

d = date.fromisoformat("2010-12-23")
print(d)

