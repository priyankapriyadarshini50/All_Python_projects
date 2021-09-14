import calendar
# print(calendar.calendar(2021))
# print(calendar.calendar(2020, w=2, l=1, c=12, m=3))
# THE BELOW METHOD DOES NOT NEED A PRINT STATEMENT
# calendar.prcal(2019)

# METHOD RETURNS THE MONTH
print(calendar.month(2021, 6, w=4, l=2))
calendar.prmonth(2021, 6)

# CHANGE THE FIRST DAY OF THE WEEK FROM MON(DEFAULT) TO ANY DAY
# print(calendar.setfirstweekday(calendar.SUNDAY))
# print(calendar.month(2021,6))
# let's change to wednesday
# print(calendar.setfirstweekday(2))
# calendar.prmonth(2021,6)

# RETURNS THE DAY OF THE WEEK IN FORM OF INT
print("The integer value of the day: ", calendar.weekday(2021, 6, 27))

# Format the week header of the month
# print(calendar.weekheader()) shows TypeError as it needed a integer argument
print(calendar.weekheader(2))  # default value
print(calendar.weekheader(3))
print(calendar.weekheader(9))
print(calendar.weekheader(6))

# CHECK IF THE YEAR IS A LEAP YEAR
print("The year 2021 is a leap", calendar.isleap(2021), sep=":")


# RETURNS THE NO OF LEAP YEARS IN A GIVEN RANGE
print("No of leap years in the given range: ", calendar.leapdays(2010, 2021))

from calendar import Calendar
# Create a object of Calendar class
c = Calendar(calendar.SUNDAY)
c1 = Calendar()
for weekday in c.iterweekdays():
    print(weekday, end=',')
print("\n")
# Iter through each date of a month
for date in c1.itermonthdates(2021, 6):
    print(date, end=" ")
print("\n")

# Iter throgh each day of a month
for day in c1.itermonthdays(2021, 6):
    print(day, end=" ")

print("\n")
for day_mn_day_wk in c1.itermonthdays2(2021, 6):
    print(day_mn_day_wk, end=" ")
print("\n")

for yr_day_wk in c1.itermonthdays3(2021, 6):
    print(yr_day_wk, end=" ")



