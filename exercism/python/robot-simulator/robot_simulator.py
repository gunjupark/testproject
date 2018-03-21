# Globals for the bearings
# Change the values as you see fit
EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.x = x
        self.y = y
        self.coordinates = (x,y)
        self.bearing = bearing

    def turn_right(self) :
        if self.bearing == EAST : self.bearing = SOUTH
        else : self.bearing -= 1

    def turn_left(self) :
        if self.bearing == SOUTH : self.bearing = EAST
        else : self.bearing += 1

    def advance(self) :
        if self.bearing == 0 : self.x+=1
        elif self.bearing == 1 : self.y+=1
        elif self.bearing == 2 : self.x-=1
        elif self.bearing == 3 : self.y-=1
        self.coordinates = (self.x,self.y)

    def simulate(self, order) :
        for i in list(order) :
            if i =='L' : self.turn_left()
            elif i =='R' : self.turn_right()
            elif i =='A' : self.advance()

