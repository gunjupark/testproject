def decode(string):
    if string is '' : return ''
    st = ''
    # i is 0
    if string[0].isdigit() : pass
    else : st += string[0]
    for i in range(1,len(string)):
        if string[i-1].isdigit() and not string[i].isdigit() :
            # i == 1
            if i is 1 : st += int(string[i-1])*string[i]
            # i > 1
            elif string[i-2].isdigit() : st += int(string[i-2:i])*string[i]
            else : st += int(string[i-1])*string[i]
        elif not string[i-1].isdigit() and not string[i].isdigit() :
            st += string[i]
    return st



def encode(string):
    if string is '' : return ''
    count =1
    st = ''
    for i in range(0,len(string)-1) :
        if string[i] == string[i+1] :
            count+=1
        else :
            if count is 1 :st += string[i]
            else : st += (str(count) +string[i])
            count =1
    if count is 1 : st+= string[-1]
    else : st += (str(count) + string[-1])
    return st

