class WeekDayError(Exception):
    def __init__(self, day, msg):
        Exception.__init__(self, msg)
        self.day = day  # here day is the property of WeekDayError class


class Weeker:
    days_in_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        self.__day = day
        for i in range(len(Weeker.days_in_week)):
            if Weeker.days_in_week[i] == self.__day:
                self.index = i
        if self.__day not in Weeker.days_in_week:
            raise WeekDayError(day, 'not in the list')

    def __str__(self):
        # Just returns the updated day in string format
        return Weeker.days_in_week[self.index]

    def add_days(self, n):
        self.index = (n % 7) + self.index

    def subtract_days(self, n):
        self.index = self.index - (n % 7)


try:
    weekday = Weeker('Thu')
    print(weekday)
    weekday.add_days(10)
    print(weekday)
    weekday.subtract_days(15)
    print(weekday)
    week1 = Weeker('AnyDay')
except WeekDayError as we:  # we is the object of WeekDayError class
    # if WeekDayError class has property(day)(it should be public),
    # then only we can access that using object(we.day) of Error class
    print(we.day, ":It does not belong to the week days list")
finally:
    print("The End!")



