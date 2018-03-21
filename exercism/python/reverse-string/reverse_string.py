# Extended Slices
# [begin:end:step]
# if begin and end are off-option statement and a step get positive value,
# sequences are going to positive way with positive step.
# if a step get negative value, then sequences are going to reverse way
# with abs(value)
def reverse(input=''):
    return input[::-1]
    '''
    l = list(input)
    l.reverse()
    input = ''
    for i in range(0,len(l)):
        input += str(l[i])
    return input
    pass
    '''
