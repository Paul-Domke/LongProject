from .artime import *



def make_solution(assign, variables, domains, constraints):
    if iscomplete(assign, variables):
        return assign


    #Remove a variable X from variables
    var = variables.pop(0)
    # TODO: pick variable using Most Constrained Variable

    # TODO: order domain values by Least Constraining Value
    for value in domains[var]:

        newassign = assign
        newassign[var] = value
        thisisok = False not in [constraint(newassign) for constraint in constraints]
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
                        newdomains[uvar].remove(uval)

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

def con_nosametimeplace(assign):
    """ Takes assignment and determines whether it has a room double booked"""
    vals = list(assign.values())
    i = 1
    for val in vals:
        for val2 in vals[i:]:
            if val['room'] == val2['room'] and val['time'].overlaps(val2['time']):
                return False
        i += 1
    return True


def con_nosameproftime(assign):
    """ Takes assignment and determines whether it has a professor in 2 place at once """
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

cons = [con_nosametimeplace, con_nosameproftime]

def get_solution(pref):
    return make_solution({}, list(pref.keys()), build_domains(pref), cons)
