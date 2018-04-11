
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

def con_level(assign):
    """
    Takes assignment values and determines if any two courses of same department
    and level occur at same time
    """
    vals = list(assign.values())
    i = 1
    for val in vals:
        for val2 in vals[i:]:
            if val['dept'] == val2['dept'] and val['level'] == val2['level'] and val['time'].overlaps(val2['time']):
                return False
        i += 1
    return True

def con_classfits(assign):
    pass

def make_class_conflict_con(courseid1, courseid2):
    pass
