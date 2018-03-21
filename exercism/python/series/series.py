def slices(series, length):
    res = []
    for i in range(0, len(series)):
        if len(series)< length or length<1 : raise ValueError("length is too long")
        elif len(series) -i >= length :
            lst = map(int,list(series[i:i+length]))
            res.append(lst)
    return res
