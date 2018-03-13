from .artime import *
from .ucs import *


example_preferences = {1:{'prof':1
                         'time':[MWF8, MWF9],
                         'room':['HNE 168', 'HNE 170'],
                         'equip': None,
                         'studentnum':30},
                      2:{'prof':1
                         'time':[MWF9, MWF10],
                         'room':['HNE 168', 'HNE 170'],
                         'equip': None,
                         'studentnum':30},}
class SchedCSP:
    def __init__(self, pref):
        self.variables = pref.keys()
        self.constraints = []
        self.pref = pref

    def add_constraint(func):
        self.constraints.append(func)

    def getinfo(var):
        return self.pref[var]

def backtracking_search(csp):
    return recursive_backtracking({}, csp)

def recursive_backtracking(assignment, csp):
    if iscomplete(assignment, csp):
         return assignment
    var = select_unassigned_variable(csp.variables, assignment, csp)
    for value in order_domain_values(var, assignment, csp):
        assignment[var] = value
        if False not in [constraint(assignment) for constraint in csp.constraints]
            result = recursive_backtracking(assignment, csp)
            if result != 'FAILURE':
                return result
            assignment.pop(var)
        else:
            assignment.pop(var)
    return 'FAILURE'

def iscomplete(assign, csp):
    """
    Determines whether assignment is a complete assignment. Returns bool.
    """
    for var in csp.variables:
        if var not in assignment:
            return False
        return True

def check_shared(times, rooms, assign):
    """
    Simple heuristic to help determine Most Constrained Variable
    Checks how many possible times and possible rooms are already being used in the assignment
    Returns shared times + shared rooms
    """
    shared = 0
    for key,val in assign:
        for time in times:
            if time.overlaps(val['time']):
                shared +=1
        if val['room'] in rooms:
            shared += 1
    return shared

def check_possible_values(times, rooms, assign):
    possible_values =[]
    for room in rooms:
        for time in times:
            possible_values.append([room, time])


def select_unassigned_variable(vars, assign, csp):
    """ Picks variable to assign next, returns reference to variable """
    mcv = None
    mcvshared = 0
    for var in vars:
        if var not in assign:
            varshared = check_shared(csp[var]['time'], csp[var]['room'], assign)
            if varshared > mcvshared:
                mcv = var
                mcvshared = varshared
    return mcv



def order_domain_values(var, assignment, csp):
    """ Chooses order to consider var's possile values, returns list of values """

def con_nosametimeplace(assign):

def con_nosameproftime(assign):

def con_classfits(assign):

def make_class_conflict_con(courseid1, courseid2):
