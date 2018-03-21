class Garden(object):
    def __init__(self, diagram, students = ['A','B','C','D','E','F','G','H','I','J','K','L']):
        self.table = {'R':'Radishes' ,'C':'Clover','G':'Grass','V':'Violets'}
        self.diagram  = diagram
        self.students = sorted(list(map(lambda x: x[0:1] , students)))

    def findst(self, student) :
        for i,name in enumerate(self.students) :
            if student[0] ==name : return i

    def plants(self, student) :
        row = self.diagram.split('\n')
        num = self.findst(student)
        temp = row[0][2*num:2*(num+1)] +row[1][2*num:2*(num+1)]
        res =[]
        for i in temp :
            res.append(self.table.get(i))
        return res


