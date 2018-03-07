from OurTime import OurTime

class TimeSlot:
    def __init__(self, start, end):
        try:
            if start.compare(end) == -1:
                self.start = start
                self.end = end
            else:
                raise Exception("Invalid Timeslot", "End time not after Start Time")
        except Exception as e:
            raise

    def __str__(self):
        return str(self.start) + " - " + str(self.end)

    def overlap(self, other):
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

    def overlapwbuffer(self, other, bday, bhour, bmin):
        buffself = TimeSlot(self.start.alter(-bday, -bhour, -bmin), self.end.alter(bday, bhour, bmin))
        buffother = TimeSlot(other.start.alter(-bday, -bhour, -bmin), other.end.alter(bday, bhour, bmin))
        return buffself.overlap(buffother)

softeng = TimeSlot(OurTime(1, 10, 0), OurTime(1, 10, 50))
databases = TimeSlot(OurTime(1, 10, 0), OurTime(1, 10, 50))
raptutorial = TimeSlot(OurTime(1, 10, 30), OurTime(1, 11, 50))
acting2 = TimeSlot(OurTime(2, 10, 20), OurTime(2, 11, 10))
rightafter = TimeSlot(OurTime(1, 10, 50), OurTime(1, 11, 0))

print(softeng)

# Should throw exceptions
#paradox = TimeSlot(OurTime(1, 10, 50), OurTime(1, 10, 0))

print(softeng.overlap(databases)) # True
print(softeng.overlap(raptutorial)) # True
print(raptutorial.overlap(databases)) # True
print(softeng.overlap(acting2)) # False
print(softeng.overlap(rightafter)) # False
print(rightafter.overlap(softeng)) # False
