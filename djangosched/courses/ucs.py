from .artime import *

MWF8 = TimePref([TimeSlot(WeekTime(1, 8, 0), WeekTime(1, 8, 50)),
                 TimeSlot(WeekTime(3, 8, 0), WeekTime(3, 8, 50)),
                 TimeSlot(WeekTime(5, 8, 0), WeekTime(5, 8, 50)),])

MWF9 = TimePref([TimeSlot(WeekTime(1, 9, 0), WeekTime(1, 9, 50)),
                 TimeSlot(WeekTime(3, 9, 0), WeekTime(3, 9, 50)),
                 TimeSlot(WeekTime(5, 9, 0), WeekTime(5, 9, 50)),])

MWF10 = TimePref([TimeSlot(WeekTime(1, 10, 0), WeekTime(1, 10, 50)),
                  TimeSlot(WeekTime(3, 10, 0), WeekTime(3, 10, 50)),
                  TimeSlot(WeekTime(5, 10, 0), WeekTime(5, 10, 50)),])

MWF11 = TimePref([TimeSlot(WeekTime(1, 11, 0), WeekTime(1, 11, 50)),
                  TimeSlot(WeekTime(3, 11, 0), WeekTime(3, 11, 50)),
                  TimeSlot(WeekTime(5, 11, 0), WeekTime(5, 11, 50)),])

MLAB = TimePref([TimeSlot(WeekTime(1, 12, 30), WeekTime(1, 17, 0))])

MSEM = TimePref([TimeSlot(WeekTime(1, 14, 0), WeekTime(1, 16, 50))])

M79 = TimePref([TimeSlot(WeekTime(1, 19, 0), WeekTime(1, 21, 50))])

MR121 = TimePref([TimeSlot(WeekTime(1, 12, 30), WeekTime(1, 13, 50)),
                  TimeSlot(WeekTime(4, 12, 30), WeekTime(4, 13, 50)),])

MR23 = TimePref([TimeSlot(WeekTime(1, 14, 0), WeekTime(1, 15, 20)),
                 TimeSlot(WeekTime(4, 14, 0), WeekTime(4, 15, 20)),])

MR34 = TimePref([TimeSlot(WeekTime(1, 15, 30), WeekTime(1, 16, 50)),
                 TimeSlot(WeekTime(4, 15, 30), WeekTime(4, 16, 50)),])

MW78 = TimePref([TimeSlot(WeekTime(1, 19, 0), WeekTime(1, 20, 20)),
                 TimeSlot(WeekTime(3, 19, 0), WeekTime(3, 20, 20)),])

TR910 = TimePref([TimeSlot(WeekTime(2, 9, 0), WeekTime(2, 10, 20)),
                  TimeSlot(WeekTime(4, 9, 0), WeekTime(4, 10, 20)),])

TR1011 = TimePref([TimeSlot(WeekTime(2, 10, 30), WeekTime(2, 11, 50)),
                   TimeSlot(WeekTime(4, 10, 30), WeekTime(4, 11, 50)),])

TLAB = TimePref([TimeSlot(WeekTime(2, 13, 0), WeekTime(2, 17, 20))])

TSEM = TimePref([TimeSlot(WeekTime(2, 14, 30), WeekTime(2, 17, 20))])

T79 = TimePref([TimeSlot(WeekTime(2, 19, 0), WeekTime(2, 21, 50))])

TF12 = TimePref([TimeSlot(WeekTime(2, 13, 0), WeekTime(2, 14, 20)),
                 TimeSlot(WeekTime(5, 13, 0), WeekTime(5, 14, 20)),])

TF23 = TimePref([TimeSlot(WeekTime(2, 14, 30), WeekTime(2, 15, 50)),
                 TimeSlot(WeekTime(5, 14, 30), WeekTime(5, 15, 50)),])

TF45 = TimePref([TimeSlot(WeekTime(2, 16, 0), WeekTime(2, 17, 20)),
                 TimeSlot(WeekTime(5, 16, 0), WeekTime(5, 17, 20)),])

WSEM = TimePref([TimeSlot(WeekTime(3, 12, 30), WeekTime(3, 3, 20))])

W79 = TimePref([TimeSlot(WeekTime(3, 19, 0), WeekTime(3, 21, 50))])

RLAB = TimePref([TimeSlot(WeekTime(4, 12, 30), WeekTime(4, 17, 0))])

RSEM = TimePref([TimeSlot(WeekTime(4, 14, 0), WeekTime(4, 16, 50))])

FLAB = TimePref([TimeSlot(WeekTime(5, 13, 0), WeekTime(5, 17, 20))])

FSEM = TimePref([TimeSlot(WeekTime(5, 14, 30), WeekTime(5, 17, 20))])


codes = {'MWF8':MWF8,
         'MWF9':MWF9,
         'MWF10':MWF10,
         'MWF11':MWF11,
         'MLAB':MLAB,
         'MSEM':MSEM,
         'M79':M79,
         'MR121':MR121,
         'MR23':MR23,
         'MR34':MR34,
         'MW78':MW78,
         'TR910':TR910,
         'TR1011':TR1011,
         'TLAB':TLAB,
         'TSEM':TSEM,
         'T79':T79,
         'TF12':TF12,
         'TF23':TF23,
         'TF45':TF45,
         'WSEM':WSEM,
         'W79':W79,
         'RLAB':RLAB,
         'RSEM':RSEM,
         'FLAB':FLAB,
         'FSEM':FSEM,
         }
