class OurTime:

    weekdays = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}

    def __init__(self, day, hour, minute):
        try:
            if day in range(0,7):
                self.day=day
            else:
                raise Exception('Invalid Date', 'Invalid Weekday')

            if hour in range(0,24):
                self.hour=hour
            else:
                raise Exception('Invalid Date', 'Invalid Hour')

            if minute in range(0,60):
                self.minute=minute
            else:
                raise Exception('Invalid Date', 'Invalid Minute')
        except Exception as e:
            raise

    def __str__(self):
        m = str(self.minute)
        if self.minute < 10:
            m = '0' + m
        return self.weekdays[self.day] + " " + str(self.hour) + ":" + m

    def compare(self, other):
        if self.day==other.day and self.hour==other.hour and self.minute==other.minute:
            return 0

        if self.day < other.day:
            return -1
        elif self.day > other.day:
            return 1

        if self.hour < other.hour:
            return -1
        elif self.hour > other.hour:
            return 1

        if self.minute < other.minute:
            return -1
        elif self.minute > other.minute:
            return 1


    def alter(self, dday, dhour, dmin):
        newmin = self.minute + dmin
        if newmin < 0:
            newmin += 60
            dhour -= 1
        elif newmin > 59:
            newmin -= 60
            dhour += 1

        newhour = self.hour + dhour
        if newhour < 0:
            newhour += 24
            dday -= 1
        elif newhour > 23:
            newhour -= 24
            dday += 1

        newday = self.day + dday
        if newday < 0:
            newday += 7
        elif newday > 6:
            newday -= 7

        return OurTime(newday, newhour, newmin)



# should throw exceptions
#OurTime(7, 0, 0)
#OurTime(0, 24, 0)
#OurTime(0, 0, 60)

monten = OurTime(1, 10, 00)
tuesten = OurTime(2, 10, 00)
montwelve = OurTime(1, 12, 00)
montenone = OurTime(1, 10, 1)

print(monten.compare(monten)) # 0
print(monten.compare(tuesten)) # -1
print(monten.compare(montwelve)) # -1
print(montwelve.compare(monten)) # 1
print(monten.compare(montenone)) # -1
print(montenone.compare(monten)) # 1
print(montenone.compare(montenone)) # 0
