WALL = 0
REDENNEMY = 1
GREENENNEMY = 2
NOTHING = 3
FINISH = 4
PERSO = 5
X = 500
Y = 500

SIZE = 32
CST = 15
NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)

class   Victory(Exception):
    pass

class   Death(Exception):
    pass
