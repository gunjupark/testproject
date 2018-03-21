def sum_of_multiples(limit, multiples):
    #initialize res
    res=0
    # class needed
    #res+= list(filter(filterfunc(lambda i,multiples),range(0,limit-1)))
    if multiples == [] : return res
    for i in range(1,limit):
        if filter_func(i, multiples) : res+=i
    return res

def filter_func(num, multiples):
    if all(list(map(lambda y: num%y, multiples))) :
        return False
    else : return True


