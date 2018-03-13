"""
Module for our custom time classes.
"""

class WeekTime:
    """
    Custom time class, records weekday, hour, and minute. Specifies time
    in context of stand-alone one-week calendar.
    Weekday is integer 0-6
    Hour is integer 0-23
    Minute is integer 0-59
    """
    weekdays = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}

    def __init__(self, day, hour, minute):
        """
        Constructor for WeekTime, checks that values are within allowable
        parameters before assigning fields.
        """
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
        """Returns string representing time in form 'Weekday Hour:Minute'"""
        m = str(self.minute)
        if self.minute < 10:
            m = '0' + m
        return self.weekdays[self.day] + " " + str(self.hour) + ":" + m

    def compare(self, other):
        """
        Compares this WeekTime to other WeekTime
        Returns:
            -1 if this time precedes other time
            0 if this time equals other time
            1 if this time comes after other time

        WARNING: This WeekTime comparison does not loop back around the standard
        week. So a time late Saturday will be seen as later than a time early Sunday.
        e.g. "Saturday 11:59".compare("Sunday 0:01") == 1
        """
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
        """
        Returns a Weektime that is dday, dhour, and dmin away from self
        """
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

        return WeekTime(newday, newhour, newmin)

class TimeSlot:
    """
    Represents a single continuous time slot, with a start WeekTime and an
    end Weektime.
    """
    def __init__(self, start, end):
        """
        Ensures start time precedes end time before assigning fields
        WARNING: WeekTime representation does not loop around, so TimeSlot
        cannot start on Saturday and end on Sunday.
        """
        try:
            if start.compare(end) == -1:
                self.start = start
                self.end = end
            else:
                raise Exception("Invalid Timeslot", "End time not after Start Time")
        except Exception as e:
            raise

    def __str__(self):
        """Returns string representation in form 'Weekday Hour:Minute - Weekday Hour:Minute'"""
        return str(self.start) + " - " + str(self.end)

    def overlaps(self, other):
        """
        Checks if this TimeSlot overlaps with other TimeSlot,
        returns True if they do and False if they do not.
        """
        # start time or end time are the same as other timeslot
        if self.start.compare(other.start) == 0 or self.end.compare(other.end) == 0:
            return True
        # start time falls within start and end time of other time slot
        if self.start.compare(other.start) == 1 and self.start.compare(other.end) == -1:
            return True
        # end time falls within start and end time of other time slot
        if self.end.compare(other.start) == 1 and self.end.compare(other.end) == -1:
            return True
        return False

    def overlapswbuffer(self, other, bday, bhour, bmin):
        """ Calls overlap with an additional buffer of bday, bhour, and bminute on both ends of both TimeSlots"""
        buffself = TimeSlot(self.start.alter(-bday, -bhour, -bmin), self.end.alter(bday, bhour, bmin))
        buffother = TimeSlot(other.start.alter(-bday, -bhour, -bmin), other.end.alter(bday, bhour, bmin))
        return buffself.overlaps(buffother)

class TimePref:
    """
    A set of timeslots that represent a full scheduling of a course over multiple weekdays
    """
    def __init__(self, slotlist):
        """ Makes sure timeslots do not overlap before instatiating time preference """
        for slot in slotlist:
            for slot2 in slotlist:
                if slot != slot2:
                    if slot.overlaps(slot2):
                        raise Exception('Invalid Time Preference','Overlapping Timeslots')

        self.slots = slotlist

    def __str__(self):
        s = ""
        for slot in self.slots[:-1]:
            s += str(slot) + ", "
        s += str(self.slots[-1])
        return s

    def overlaps(self, other):
        """ Check if I conflict with other TimePref """
        for myslot in self.slots:
            for urslot in other.slots:
                if myslot.overlaps(urslot):
                    return True
        return False

    def overlapswbuffer(self, other, bday, bhour, bmin):
        """ Check if I conflict with other TimePref, applying buffers to ends of slots"""
        for myslot in self.slots:
            for urslot in other.slots:
                if myslot.overlapswbuffer(urslot, bay, bhour, bmin):
                    return True
        return False
