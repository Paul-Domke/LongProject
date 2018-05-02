
def con_nosametimeplace(assign):
    """ Takes assignment and determines whether it has a room double booked """
    result = 0
    vals = list(assign.values())
    i = 1
    for val in vals:
        for val2 in vals[i:]:
            if not val2['time'].equals(val['time']):
                break
            if val['room'] == val2['room'] and val['time'].overlaps(val2['time']):
                result += 100
        i += 1
    return result


def con_nosameproftime(assign):
    """ Takes assignment and determines whether it has a professor in 2 places at once """
    result = 0
    vals = list(assign.values())
    i = 1
    for val in vals:
        for val2 in vals[i:]:
            if not val2['time'].equals(val['time']):
                break
            if val['prof'] == val2['prof'] and val['time'].overlaps(val2['time']):
                result += 100
        i += 1
    return result

def con_level(assign):
    """
    Takes assignment values and determines if any two courses of same department
    and level occur at same time
    """
    result = 0
    vals = list(assign.values())
    i = 1
    for val in vals:
        for val2 in vals[i:]:
            if not val2['time'].equals(val['time']):
                break
            if val['dept'] == val2['dept'] and val['level'] == val2['level'] and val['time'].overlaps(val2['time']):
                result += 10
        i += 1
    return result

def con_classfits(assign):
    pass

def make_class_conflict_con(courseid1, courseid2):
    pass
