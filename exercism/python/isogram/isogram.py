def is_isogram(string):
    string = string.lower()
    l = list(string)
    for i in range(0,len(l)) :
        if l.count(l[i]) > 1 and l[i] is not ' ' and l[i] is not '-':
            return False
    return True
    pass
