from .artime import *
import pytest

def test_WeekTime_bigvalues():

    with pytest.raises(Exception):
        WeekTime(7, 0, 0)
    with pytest.raises(Exception):
        WeekTime(0, 24, 0)
    with pytest.raises(Exception):
        WeekTime(0, 0, 60)

def test_WeekTime_negvalues():
    with pytest.raises(Exception):
        WeekTime(-1, 0, 0)
    with pytest.raises(Exception):
        WeekTime(0, -1, 0)
    with pytest.raises(Exception):
        WeekTime(0, 0, -1)

def test_WeekTime_compare():
    monten = WeekTime(1, 10, 00)
    tuesten = WeekTime(2, 10, 00)
    montwelve = WeekTime(1, 12, 00)
    montenone = WeekTime(1, 10, 1)

    assert monten.compare(monten) == 0
    assert monten.compare(tuesten) == -1
    assert monten.compare(montwelve) == -1
    assert montwelve.compare(monten) == 1
    assert monten.compare(montenone) == -1
    assert montenone.compare(monten) == 1
    assert montenone.compare(montenone) == 0

softeng = TimeSlot(WeekTime(1, 10, 0), WeekTime(1, 10, 50))
databases = TimeSlot(WeekTime(1, 10, 0), WeekTime(1, 10, 50))
raptutorial = TimeSlot(WeekTime(1, 10, 30), WeekTime(1, 11, 50))
acting2 = TimeSlot(WeekTime(2, 10, 20), WeekTime(2, 11, 10))
rightafter = TimeSlot(WeekTime(1, 10, 50), WeekTime(1, 11, 0))


def test_TimeSlot_str():
    assert str(softeng) == 'Monday 10:00 - Monday 10:50'

def test_TimeSlot_init():
    with pytest.raises(Exception):
        paradox = TimeSlot(WeekTime(1, 10, 50), WeekTime(1, 10, 0))

def test_TimeSlot_overlap():
    assert softeng.overlap(databases) == True
    assert softeng.overlap(raptutorial) == True
    assert raptutorial.overlap(databases) == True
    assert softeng.overlap(acting2) == False
    assert softeng.overlap(rightafter) == False
    assert rightafter.overlap(softeng) == False



def test_TimePref_init():
    with pytest.raises(Exception):
        TimePref([TimeSlot(WeekTime(1, 10, 0), WeekTime(1, 10, 50)),
                  TimeSlot(WeekTime(1, 10, 0), WeekTime(1, 10, 50)),])
    with pytest.raises(Exception):
        TimePref([TimeSlot(WeekTime(1, 10, 0), WeekTime(1, 10, 50)),
                  TimeSlot(WeekTime(1, 10, 30), WeekTime(1, 11, 20)),])

    TimePref([TimeSlot(WeekTime(1, 10, 0), WeekTime(1, 10, 50)),
              TimeSlot(WeekTime(1, 10, 50), WeekTime(1, 11, 50)),])

def test_TimePref_str():
    tp = TimePref([TimeSlot(WeekTime(1, 10, 0), WeekTime(1, 10, 50)),
                   TimeSlot(WeekTime(3, 10, 0), WeekTime(3, 10, 50)),
                   TimeSlot(WeekTime(5, 10, 0), WeekTime(5, 10, 50)),])
    assert str(tp) == 'Monday 10:00 - Monday 10:50, Wednesday 10:00 - Wednesday 10:50, Friday 10:00 - Friday 10:50'

def test_TimePref_overlap():
    tp = TimePref([TimeSlot(WeekTime(1, 10, 0), WeekTime(1, 10, 50)),
                   TimeSlot(WeekTime(3, 10, 0), WeekTime(3, 10, 50)),
                   TimeSlot(WeekTime(5, 10, 0), WeekTime(5, 10, 50)),])

    tpconflict = TimePref([TimeSlot(WeekTime(2, 10, 0), WeekTime(2, 10, 50)),
                           TimeSlot(WeekTime(4, 10, 0), WeekTime(4, 10, 50)),
                           TimeSlot(WeekTime(5, 10, 30), WeekTime(5, 11, 20)),])

    notconflict = TimePref([TimeSlot(WeekTime(2, 10, 0), WeekTime(2, 10, 50)),])

    assert tp.overlap(tp) == True
    assert tp.overlap(tpconflict) == True
    assert tp.overlap(notconflict)== False
