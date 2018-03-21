class Allergies(object):
    def __init__(self, score):
        self.__score = score
        self.res = []
        # binary translated
        st = bin(self.__score)[2:]
        # string formating( right sorting + black=0 + 8chr parsing)
        st ="{0:0>8}".format(st[-8:-1]+st[-1])
        if int(st[7]) : self.res.append('eggs')
        if int(st[6]) : self.res.append('peanuts')
        if int(st[5]) : self.res.append('shellfish')
        if int(st[4]) : self.res.append('strawberries')
        if int(st[3]) : self.res.append('tomatoes')
        if int(st[2]) : self.res.append('chocolate')
        if int(st[1]) : self.res.append('pollen')
        if int(st[0]) : self.res.append('cats')

    def is_allergic_to(self, item):
        if item in self.lst : return True
        else : return False

    # @: decorator (function's functionality extend)
    # http://hamait.tistory.com/827
    # usage : get, set function replaced by @property
    @property
    def lst(self):
        return self.res


