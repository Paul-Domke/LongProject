
def all_cons(times):
    """ Takes assignment and determines whether it has a room double booked """
    result = 0
    for time in times:
        vals = times[time]
        i = 1
        for val in vals:
            for val2 in vals[i:]:
                if val['room'] == val2['room']:
                    result += 100
                if val['prof'] == val2['prof']:
                    result += 100
                if val['dept'] == val2['dept'] and val['level'] == val2['level']:
                    result += 10
            i += 1

    tkeys = times.keys()
    j = 1
    for time in tkeys:
        for time2 in tkeys[j:]:
            if time.overlaps(time2):
                for val in times[time]:
                    for val2 in times[time2]:
                        if val['room'] == val2['room']:
                            result += 100
                        if val['prof'] == val2['prof']:
                            result += 100
                        if val['dept'] == val2['dept'] and val['level'] == val2['level']:
                            result += 10
            else:
                break

    return result
