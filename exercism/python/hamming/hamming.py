def distance(strand_a, strand_b):
    count=0
    if len(strand_a) is not len(strand_b):
        raise ValueError("length mismatched")
    for i in range(0,len(strand_a)):
        if strand_a[i] != strand_b[i] : count+=1
    return count





#DNA strand rule applied
    '''
    la = list(strand_a).sort()
    lb = list(strand_b).sort()
    for s in range(['A','C','G','T'])
        l1.append(la.count(s))
        l2.append(lb.count(s))
    if(): 
    '''
