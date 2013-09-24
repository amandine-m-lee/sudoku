#I have this idea to start a sudoku solver. I think we want a board to start.
#For consistency, everything with be 1 index
#Some other design thoughts -

class SudokuUniquenessException(Exception):
    pass
class Board(object):

    def __init__(self):
        pass

class Unit(object):
    def __init__(self, start_nums={}):
        self.nums = set(nums)

    def free(num):
        return num not in self.nums

    def add(num):
        if num in self.nums:
            print "Number conflict" #Could give more informative error
            raise SudokuUniquenessException("{} not unique".format(num)) 

class Box(Unit):

    def __init__(self, xloc, yloc, nums=[]):
        self.nums = set(nums)
        self.xloc = xloc
        slef.yloc = yloc


class Row(Unit):
    
    def __init__(self, rownum):
        self.index = rownum #Needs to be within 0 and 8

class Column(Unit):

    def __init__(self, colnum):
        self.index = colnum #Needs to be between 0 and 8

"""Questions:
    - Should I make my own error for when a number does not work?
    - Start with user solving, add AI later
    - How exactly does inheritance work?
    - Put in safeguards to make sure the indexy attributes are in the correct range"""






