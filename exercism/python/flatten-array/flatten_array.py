def flatten(iterable):
    res = []
    if () in iterable : 
        return res
    for k in range(iterable.count(None)) :
        iterable.remove(None)
    for i in range(len(iterable)) :
        if type(iterable[i]) == type([]) :
            res += flatten(iterable[i])
        else :
            res += [iterable[i]]
    return res

