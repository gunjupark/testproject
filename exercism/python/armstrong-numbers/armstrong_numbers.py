def is_armstrong(number):
    res =0
    stnum =  str(number)
    length = len(stnum)
    for i in range(0,length) :
        res += (int(stnum[i])**length)
    return number == res
