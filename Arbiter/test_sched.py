from .sched import *
from .ucs import *
import pytest

example_preferences = {1:{'prof':1,
                         'time':[MWF8, MWF9],
                         'room':['HNE 168'],
                         'equip': None,
                         'studentnum':30},
                      2:{'prof':2,
                         'time':[MWF8],
                         'room':['HNE 168'],
                         'equip': None,
                         'studentnum':30},}

goodass = {1:{'time':MWF9, 'room':'HNE 168', 'prof':1}, 2:{'time':MWF8, 'room':'HNE 168', 'prof':2}}

def test_iscomplete():
    a1 = {1:{'time':MWF9, 'room':'HNE 168'}}
    a2 = {1:{'time':MWF9, 'room':'HNE 168'}, 2:{'time':MWF8, 'room':'HNE 168'}}

    assert iscomplete(a1, example_preferences.keys()) == False
    assert iscomplete(a2, example_preferences.keys()) == True

def test_build_domains():
    d = build_domains(example_preferences)
    assert d == {1:[{'prof':1, 'room':'HNE 168', 'time':MWF8},
                    {'prof':1, 'room':'HNE 168', 'time':MWF9}],
                 2:[{'prof':2, 'room':'HNE 168', 'time':MWF8}]}

def test_con_nosametimeplace():
    badass = {1:{'time':MWF9, 'room':'HNE 168', 'prof':1}, 2:{'time':MWF9, 'room':'HNE 168', 'prof':2}}

    assert con_nosametimeplace(goodass) == True
    assert con_nosametimeplace(badass) == False

def test_con_nosameproftime():
    badass = {1:{'time':MWF8, 'room':'HNE 170', 'prof':2}, 2:{'time':MWF8, 'room':'HNE 168', 'prof':2}}

    assert con_nosameproftime(goodass) == True
    assert con_nosameproftime(badass) == False

def test_get_solution():
    assert get_solution(example_preferences) == goodass
