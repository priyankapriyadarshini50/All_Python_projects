def two_digits(time):
    time1 = str(time)
    if len(time1) == 1:
        return '0'+ time1
    else:
        return time1


class Timer:

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        hr = two_digits(self.__hours)
        mn = two_digits(self.__minutes)
        sc = two_digits(self.__seconds)
        return str(hr)+":"+str(mn)+":"+str(sc)



    def next_second(self):
        self.__seconds += 1
        if self.__seconds > 59:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes > 59:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours > 23:
                    self.__hours = 0

    def previous_second(self):
        self.__seconds -= 1
        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes < 0:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours < 0:
                    self.__hours = 23


#timer = Timer(23, 59, 59)
#print(timer)
#timer.next_second()
#print(timer)
#timer.previous_second()
#print(timer)

timer1 = Timer(15, 34, 59)
print(timer1)
timer1.next_second()
print(timer1)
timer1.previous_second()
print(timer1)
