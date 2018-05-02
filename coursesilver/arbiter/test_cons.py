from .cons import *
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

goodass = {1:{'time':MWF9, 'room':'HNE 168', 'prof':1, 'dept':'CS', 'level':'Introductory'},
           2:{'time':MWF8, 'room':'HNE 168', 'prof':2, 'dept':'CS', 'level':'Introductory'}}

def test_con_nosametimeplace():
    badass = {1:{'time':MWF9, 'room':'HNE 168', 'prof':1}, 2:{'time':MWF9, 'room':'HNE 168', 'prof':2}}

    assert con_nosametimeplace(goodass) == True
    assert con_nosametimeplace(badass) == False

def test_con_nosameproftime():
    badass = {1:{'time':MWF8, 'room':'HNE 170', 'prof':2}, 2:{'time':MWF8, 'room':'HNE 168', 'prof':2}}

    assert con_nosameproftime(goodass) == True
    assert con_nosameproftime(badass) == False

def test_con_level():
    badass = {1:{'time':MWF9, 'room':'HNE 170', 'prof':1, 'dept':'CS', 'level':'Introductory'},
              2:{'time':MWF9, 'room':'HNE 168', 'prof':2, 'dept':'CS', 'level':'Introductory'}}

    assert con_level(goodass) == True
    assert con_level(badass) == False
