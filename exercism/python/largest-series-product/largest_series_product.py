def largest_product(series, size):
    if size ==0 : return 1
    return max(list(map(mul,slices(series, size))))

def mul(lst) :
    res =1
    for i in range(0,len(lst)) :
        res*=lst[i]
    return res

def slices(series, length):
    res = []
    for i in range(0, len(series)):
        if len(series)< length or length<1 :
            raise ValueError("length is too long")
        elif len(series) -i >= length :
            lst = list(map(int,list(series[i:i+length])))
            res.append(lst)
    return res
