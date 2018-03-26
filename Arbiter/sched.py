from .artime import *
import copy


def get_solution(pref):
    """
    This is the function to call, what this whole module is forself.
    It takes a python dictionary representing preferences, which must have
    entries of the following form:

    { COURSE_IDENTIFIER:{'prof':PROFESSOR_IDENTIFIER,
                         'time':LIST_OF_TIMES,
                         'room':LIST_OF_ROOMS,},}

    It will return a solution also in the form of a dictionary:

    { COURSE_IDENTIFIER:{'time':ASSIGNED_TIME,
                         'room':ASSIGNED_ROOM},}

    If there is no possible solution it will return the string 'FAILURE'
    """
    cons = [con_nosametimeplace, con_nosameproftime]
    return make_solution({}, list(pref.keys()), build_domains(pref), cons)

def make_solution(assign, variables, domains, constraints):
    #print('top', assign)
    if iscomplete(assign, variables):
        return assign


    # Remove a variable var from variables
    # pick variable using Most Constrained Variable
    var = get_mcv(domains)
    variables.remove(var)
    #print('var', var)


    # order domain values by Least Constraining Value
    vals = sorted(domains.pop(var), key=lambda val:how_constraining(val, domains))

    for value in vals:
        #print('value',value)
        newassign = copy.deepcopy(assign)
        newassign[var] = value
        #thisisok = False not in [constraint(newassign) for constraint in constraints]
        # if var = value is consistent with assign according to the constraints then
        thisisok = True
        if thisisok:
            #print('got to 1')
            # Add var = value to assign
            assign = newassign
            newdomains = copy.deepcopy(domains)
            # for uvar in variables (i.e., uvar an unassigned variable), uvar − − − var (i.e., uvar a neighbor of var in the constrained graph) do
            #       Remove values for uvar from newdomains[uvar] that are inconsistent with assign
            for uvar in variables:
                #print('got to 2')
                for uval in newdomains[uvar]:
                    uassign = copy.deepcopy(newassign)
                    uassign[uvar] = uval
                    #print(uvar, uval, [constraint(uassign) for constraint in constraints])
                    if False in [constraint(uassign) for constraint in constraints]:
                        #print('got to 3')
                        newdomains[uvar].remove(uval)
                        #print(newdomains)

            # if for all uvar ∈ variables, uvar − − − var, we have newdomains (uvar ) not empty then
            if [] not in newdomains.values():
                result = make_solution(newassign, variables, newdomains, constraints)
                if result != 'FAILURE':
                    return result

            #Remove var = value from assign

    return 'FAILURE'

def iscomplete(assign, variables):
    """
    Determines whether assignment is a complete assignment. Returns bool.
    """
    for var in variables:
        if var not in assign:
            return False
    return True

def build_domains(pref):
    domains = {course:[] for course in pref}
    for course in pref:
        for room in pref[course]['room']:
            for time in pref[course]['time']:
                domains[course].append({'prof':pref[course]['prof'],
                                        'room':room,
                                        'time':time})
    return domains

def get_mcv(domains):
    mcv = None
    smallest = 1000
    for key in domains:
        d = len(domains[key])
        if d < smallest:
            smallest = d
            mcv = key
    return mcv

def how_constraining(val, domains):
    out = 0
    for domain in domains.values():
        for other in domain:
            if val['room'] == other['room'] or val['prof'] == other['prof']:
                if val['time'].overlaps(other['time']):
                    out += 1
    return out


def con_nosametimeplace(assign):
    """ Takes assignment and determines whether it has a room double booked """
    vals = list(assign.values())
    i = 1
    for val in vals:
        for val2 in vals[i:]:
            if val['room'] == val2['room'] and val['time'].overlaps(val2['time']):
                return False
        i += 1
    return True


def con_nosameproftime(assign):
    """ Takes assignment and determines whether it has a professor in 2 places at once """
    vals = list(assign.values())
    i = 1
    for val in vals:
        for val2 in vals[i:]:
            if val['prof'] == val2['prof'] and val['time'].overlaps(val2['time']):
                return False
        i += 1
    return True

def con_classfits(assign):
    pass

def make_class_conflict_con(courseid1, courseid2):
    pass
