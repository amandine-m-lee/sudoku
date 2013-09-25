#I have this idea to start a sudoku solver. I think we want a board to start.
#For consistency, everything with be 1 index
#Some other design thoughts -

class SudokuUniquenessException(Exception):
    pass
class Board(object):

    def __init__(self):

        self.cols = [Column(i) for i in range(9)]
        self.rows = [Row(i) for i in range(9)]
        self.boxes = [Box(i) for i in range(9)]


        pass

    def print_board(self):
        print('-'*19)
        colnum = 0
        for _ in range(3):
            for _ in range(3):
                subrows = [' '.join(map(str, self.cols[colnum].nums[i:i+3])) for i in range(3)]
                print('|' + '|'.join(subrows) + '|')
                colnum += 1 

            print('-'*19)



class Unit(object):
    def __init__(self, start_nums):
        self.nums = start_nums

    def free(num):
        return num not in self.nums

    def add(num):
        if num in self.nums:
            raise SudokuUniquenessException("{} not unique".format(num)) 

class Box(Unit):

    def __init__(self, index, start_nums=[0 for _ in range(9)]):
        super().__init__(start_nums)
        self.index = index

class Row(Unit):
    
    def __init__(self, rownum, start_nums=[0 for _ in range(9)]):
        super().__init__(start_nums)
        self.index = rownum #Needs to be within 0 and 8

class Column(Unit):

    def __init__(self, colnum, start_nums=[0 for _ in range(9)]):
        super().__init__(start_nums)
        self.index = colnum #Needs to be between 0 and 8

"""Questions/Thoughts:
    - Should I make my own error for when a number does not work?
    - Start with user solving, add AI later
    - How exactly does inheritance work?
    - Put in safeguards to make sure the indexy attributes are in the correct range
    - Do this in Python 3?
    - Refactor where type is just a member of unit? Really they are the same. maybe I'll went different print methods though"""






