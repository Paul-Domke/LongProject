from .artime import *
import copy
from .cons import *
import random
import math
from sortedcontainers import SortedDict
from decimal import Decimal


def get_solution(pref):

    solution = get_annealed(pref)

    return solution


def get_annealed(pref):
    """
    Sets up annealer by making a random solution and then passing parameters
    to anneal_solution
    """

    cons = [all_cons]
    times = get_times_dict(pref)
    rand_sol = random_solution({}, list(pref.keys()), build_domains(pref), times)
    return anneal_solution(rand_sol, list(pref.keys()), build_domains(pref), cons, times)

def random_solution(assign, variables, domains, times):

    """
    Creates a fully random solution by assigning each variable a random value
    from its domain
    """
    for variable in variables:

        val =  random.choice(domains[variable])
        assign[variable] = val
        times[val['time']].append(val)

    return assign

def acceptance_probability(old_cost, new_cost, T):
    """
    Calculates the acceptance_probability of the annealing algorithm as a
    function of e^((old_cost-new_cost)/Temperature)
    """
    return Decimal(math.e) ** Decimal((old_cost-new_cost)/T)


def get_neighbor(solution, variables, domains, times):

    """
    Finds a neighboring solution by picking a varible at random and changing
    its assignment to a random different value in its domain.
    """
    var = random.choice(variables)


    #print('REMOVE', '\n', solution[var]['time'], times[solution[var]['time']],'\n\n', solution[var], '\n')
    times[solution[var]['time']].remove(solution[var])

    #print(var, var)
    dom = domains[var]
    #print(domains[var] == dom)
    #print(solution[var])
    #print(dom)
    if len(dom)>1:
        dom.remove(solution[var])
    neighbor = dict(solution)

    val = random.choice(dom)
    neighbor[var] = val
    #print('ADD', '\n', val['time'], times[val['time']], '\n\n', val, '\n')
    times[val['time']].append(val)
    dom.append(solution[var])
    return neighbor, solution[var], val

def anneal_solution(solution, variables, domains, constraints, times):
    "Uses simulated annealing to make the best possible solution"
    old_cost = sum([constraint(times) for constraint in constraints])

    T = 1.0
    T_min = 0.00001
    alpha = 0.9
    while T > T_min:
        i = 1
        while i <= 200:

            new_sol, was_removed, was_added = get_neighbor(solution, variables, domains, times)
            new_cost = sum([constraint(times) for constraint in constraints])

            ap = acceptance_probability(old_cost, new_cost, T)
            if ap > random.random():
                solution = new_sol
                old_cost = new_cost

            else:
                times[was_removed['time']].append(was_removed)
                times[was_added['time']].remove(was_added)

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
                    val['enemies'] += "<br>"+val2['name']

                if val2['enemies'] == "":
                    val2['enemies'] += val['name']
                else:
                    val2['enemies'] += "<br>"+val['name']
        i += 1


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


def get_times_dict(pref):
    times = set()
    for course in pref:
        for time in pref[course]['time']:
            times.add(time)
    return SortedDict({time:[] for time in times})
