class School(object):
    def __init__(self, name):
        self.name = name
        # Cannot using [set()]*9
        self.sts = [
            set(),set(),set(),
            set(),set(),set(),
            set(),set(),set()
        ]

    def add(self,__student,__grade) :
        st = self.sts[(__grade)-1]
        st.add(__student)

    def grade(self, __grade) :
        return tuple(self.sts[(__grade)-1])

    def sort(self):
        res = []
        for i in range(9) :
            if self.sts[i] == set() : continue
            res.append((i+1 ,) + (tuple(sorted(list(self.sts[i]))),))
        return res
