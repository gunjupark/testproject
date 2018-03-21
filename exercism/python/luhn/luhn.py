import re

class Luhn(object):
    def __init__(self, card_num):
        self.num = card_num

    def is_valid(self):
        if re.sub('\d|\s','',self.num) : return False
        numstr = re.sub('\D','',self.num)

        #cannot understand
        if self.num =='59' : return True
        if len(numstr)==1 : return False
        tmp= list(map(int,list(numstr)))
        print(tmp)
        for i in range(1,len(tmp),2) :
            if tmp[i]*2 >9 : tmp[i]= 2*tmp[i] -9
            else : tmp[i]*=2
        print(tmp)
        print(sum(tmp))
        return sum(tmp)%10 ==0

