from .artime import *
import copy
from .cons import *
import random
import math
from sortedcontainers import SortedDict


def get_solution(pref):
    """
    This is the function to call, what this whole module is for.
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
    """
    solution = ideal_solution(pref)

    if solution == 'FAILURE':
        solution = strict_solution(pref)
    """
    solution = get_annealed(pref)

    return solution

def ideal_solution(pref):
    cons = [con_nosametimeplace, con_nosameproftime, con_level]
    return make_solution({}, list(pref.keys()), build_domains(pref), cons)

def strict_solution(pref):
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
                    if sum([constraint(uassign) for constraint in constraints]) > 0:
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

def get_annealed(pref):
    """
    Sets up annealer by making a random solution and then passing parameters
    to anneal_solution
    """
    cons = [con_nosametimeplace, con_nosameproftime, con_level]
    rand_sol = random_solution({}, list(pref.keys()), build_domains(pref))
    return anneal_solution(rand_sol, list(pref.keys()), build_domains(pref), cons)

def random_solution(assign, variables, domains):
    """
    Creates a fully random solution by assigning each variable a random value
    from its domain
    """
    for variable in variables:
        assign[variable] = random.choice(domains[variable])
    return assign

def acceptance_probability(old_cost, new_cost, T):
    """
    Calculates the acceptance_probability of the annealing algorithm as a
    function of e^((old_cost-new_cost)/Temperature)
    """
    return math.e ** ((old_cost-new_cost)/T)

def get_neighbor(solution, variables, domains):
    """
    Finds a neighboring solution by picking a varible at random and changing
    its assignment to a random different value in its domain.
    """
    var = random.choice(variables)
    #print(var, var)
    dom = domains[var]
    #print(domains[var] == dom)
    #print(solution[var])
    #print(dom)
    if len(dom)>1:
        dom.remove(solution[var])
    neighbor = dict(solution)
    neighbor[var] = random.choice(dom)
    dom.append(solution[var])
    return neighbor

def anneal_solution(solution, variables, domains, constraints):
    "Uses simulated annealing to make the best possible solution"
    sorted_sol = SortedDict(lambda x: solution[x]['time'], solution)
    old_cost = sum([constraint(sorted_sol) for constraint in constraints])
    T = 1.0
    T_min = 0.00001
    alpha = 0.9
    while T > T_min:
        i = 1
        while i <= 100:
            new_sol = get_neighbor(solution, variables, domains)
            new_sorted_sol = SortedDict(lambda x: new_sol[x]['time'], new_sol)
            new_cost = sum([constraint(new_sorted_sol) for constraint in constraints])
            ap = acceptance_probability(old_cost, new_cost, T)
            if ap > random.random():
                solution = new_sol
                old_cost = new_cost
            i += 1
        T = T*alpha
    mark_conflicts(solution, constraints)
    return solution

def mark_conflicts(assign, constraints):
    """
    Marks variables not fitting constraints
    """
    vals = list(assign.values())
    i = 1
    for val in vals:
        for val2 in vals[i:]:
            if (val['prof'] == val2['prof'] or val['room'] == val2['room']) and val['time'].overlaps(val2['time']):
                val['conflict'] = True
                val2['conflict'] = True

                if val['enemies'] == "":
                    val['enemies'] += val2['name']
                else:
                    val['enemies'] += ", "+val2['name']

                if val2['enemies'] == "":
                    val2['enemies'] += val['name']
                else:
                    val2['enemies'] += ", "+val['name']
        i += 1


def iscomplete(assign, variables):
    """
    Determines whether assignment is a complete assignment. Returns bool.
    """
    for var in variables:
        if var not in assign:
            return False
    return True

def build_domains(pref):
    """
    Given a set of course preferences, generates complete domains of every
    varible. Here variables are courses and each domain is a combination of a
    specific time and course. Size of each domain is therefore
    # of possible rooms * # of possible times
    """
    domains = {course:[] for course in pref}
    for course in pref:
        for room in pref[course]['room']:
            for time in pref[course]['time']:
                domains[course].append({'name':pref[course]['name'],
                                        'prof':pref[course]['prof'],
                                        'room':room,
                                        'time':time,
                                        'dept':pref[course]['dept'],
                                        'level':pref[course]['level'],
                                        'conflict':False,
                                        'enemies':''})
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
