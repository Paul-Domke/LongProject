from .sched import *
from .ucs import *
import pytest

example_preferences = {1:{'prof':1,
                         'time':[MWF8, MWF9],
                         'room':['HNE 168'],
                         'dept':'CS',
                         'level': 'Introductory'},
                      2:{'prof':2,
                         'time':[MWF8],
                         'room':['HNE 168'],
                         'dept':'CS',
                         'level': 'Introductory'}}

def test_iscomplete():
    a1 = {1:{'time':MWF9, 'room':'HNE 168'}}
    a2 = {1:{'time':MWF9, 'room':'HNE 168'}, 2:{'time':MWF8, 'room':'HNE 168'}}

    assert iscomplete(a1, example_preferences.keys()) == False
    assert iscomplete(a2, example_preferences.keys()) == True

def test_build_domains():
    d = build_domains(example_preferences)
    assert d == {1:[{'prof':1, 'room':'HNE 168', 'time':MWF8, 'dept':'CS', 'level':'Introductory'},
                    {'prof':1, 'room':'HNE 168', 'time':MWF9, 'dept':'CS', 'level':'Introductory'}],
                 2:[{'prof':2, 'room':'HNE 168', 'time':MWF8, 'dept':'CS', 'level':'Introductory'}]}

def test_get_mcv():
    d = build_domains(example_preferences)

    assert get_mcv(d) == 2

def test_how_constraining():
    d = build_domains(example_preferences)
    vals = d.pop(1)

    assert how_constraining(vals[0], d) == 1
    assert how_constraining(vals[1], d) == 0

def test_get_solution():
    solution = get_solution(example_preferences)
    assert solution[1]['room'] == 'HNE 168'
    assert solution[2]['room'] == 'HNE 168'
    assert solution[1]['time'].equals(MWF9)
    assert solution[2]['time'].equals(MWF8)
