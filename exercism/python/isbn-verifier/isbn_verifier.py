import re

def verify(isbn):
    val=0
    st = re.sub('[A-W,Y,Z-]','',isbn.upper())
    if(len(st) is not 10 or st[0:9].count('X')>0) : return False
    else:
        for i in range(0,10) :
            if st[i] is 'X' : val += 10
            else : val += (int(st[i])*(10-i))
        if val%11 is 0 : return True
        else : return False
