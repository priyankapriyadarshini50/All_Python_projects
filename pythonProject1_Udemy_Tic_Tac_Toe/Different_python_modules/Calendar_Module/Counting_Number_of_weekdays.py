from calendar import Calendar

c = Calendar()
counter = 0
for week in c.monthdays2calendar(2021, 7):
    print(week)
    for day, week_day in week:
        print(week_day)
        if (week_day == 0) and (day != 0):
            counter += 1
print("The number of MOndays in a July, 2021: ", counter)

from calendar import Calendar

class MyCalendar(Calendar):

    def __init__(self):
        super().__init__()


    def count_weekday_in_year(self, year, weekday):
        number_of_days = 0
        for month in range(1, 13):
            for week in c.monthdays2calendar(year, month):

                for day,week_day in week:
                    if (week_day == weekday) and (day != 0):
                        number_of_days += 1
        return number_of_days


c1 = MyCalendar()
print(f"The total number of wekdays in a year: ", c1.count_weekday_in_year(2000, 6))

