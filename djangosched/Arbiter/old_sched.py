"""
Module to hold scheduling algorithm.
"""

from .artime import *

class SchedCSP:
    def __init__(self, pref):
        self.pref = pref
        self.variables = pref.keys()
        self.domains = build_domains(pref)
        self.constraints = []


    def add_constraint(func):
        self.constraints.append(func)


def backtracking_search(csp):
    return recursive_backtracking({}, csp)

def recursive_backtracking(assignment, csp):
    """
    Recursive backtracking search to create complete solution for CSP
    """
    if iscomplete(assignment, csp):
         return assignment
    var = select_unassigned_variable(csp.variables, assignment, csp)
    for value in order_domain_values(var, assignment, csp):
        assignment[var] = value
        if False not in [constraint(assignment) for constraint in csp.constraints]:
            result = recursive_backtracking(assignment, csp)
            if result != 'FAILURE':
                return result
            assignment.pop(var)
        else:
            assignment.pop(var)
    return 'FAILURE'

def get_solution(assign, variables, domains, constraints):
    if iscomplete(assign):
        return assign


    #Remove a variable X from variables
    var = variables.pop(0)
    # TODO: pick variable using Most Constrained Variable

    # TODO: order domain values by Least Constraining Value
    for value in domains[var]:

        newassign = assign
        newassign[var] = value
        #thisisok = False not in [constraint(newassign) for constraint in constraints]
        # if var = value is consistent with assign according to the constraints then
        thisisok = True
        if thisisok:
            # Add var = value to assign
            assign = newassign
            newdomains = domains
            # for uvar in variables (i.e., uvar an unassigned variable), uvar − − − var (i.e., uvar a neighbor of var in the constrained graph) do
            #       Remove values for uvar from newdomains(uvar ) that are inconsistent with assign
            for uvar in variables:
                for uval in newdomains[uvar]:
                    uassign = newassign
                    uassign[uvar] = uval
                    if False in [constraint(uassign) for constraint in constraints]:
                        newdomain[uvar].remove(uval)

            # if for all uvar ∈ variables, uvar − − − var, we have newdomains (uvar ) not empty then
            if [] not in newdomains.values():
                result = get_solution(newassign, variables, newdomains, constraints)
                if result != 'FAILURE':
                    return result

            Remove var = value from assign

    return 'FAILURE'

def iscomplete(assign, csp):
    """
    Determines whether assignment is a complete assignment. Returns bool.
    """
    for var in csp.variables:
        if var not in assign:
            return False
    return True

def check_shared(times, rooms, assign):
    """
    DEPRECATED
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

def get_possible_values(times, rooms, assign):
    """
    Generates list of possible values given set of times and rooms and the current assignment
    """
    possible_values =[]
    for room in rooms:
        for time in times:
            noconflicts = True
            for key,val in assign:
                if room == val['room']:
                    if time.overlaps(val['time']):
                        noconflicts = False
            if noconflicts:
                possible_values.append([room, time])

    return possible_values

def deprecated_select_unassigned_variable(vars, assign, csp):
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

def select_unassigned_variable(vars, assign, csp):
    """ Picks variable to assign next, returns reference to variable """
    mcv = None
    mcvvals = 100
    for var in vars:
        if var not in assign:
            varvals = len(check_possible_values(csp[var]['time'], csp[var]['room'], assign))
            if varvals > mcvvals:
                mcv = var
                mcvvals = varvals
    return mcv

def order_domain_values(var, assignment, csp):
    """ Chooses order to consider var's possible values, returns list of values """

def con_nosametimeplace(assign):
    """ Takes current assignment and domains, and removes values from domains that are no longer feasible """
    vals = assign.values():
    i = 0
    for val in vals:
        for val2 in vals[i:]:
            if val['room'] == val2['room'] and val[1].overlaps(val2[1]):
                return False
        i += 1
    return True


def con_nosameproftime(assign):
    """ Takes current assignment and domains, and removes values from domains that are no longer feasible """
    vals = assign.values():
    i = 0
    for val in vals:
        for val2 in vals[i:]:
            if val[1].overlaps(val2[1]):
                if
        i += 1

def con_classfits(assign):
    pass

def make_class_conflict_con(courseid1, courseid2):
    pass
