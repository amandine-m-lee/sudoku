#I have this idea to start a sudoku solver. I think we want a board to start.
#For consistency, everything with be 1 index
#Some other design thoughts -

class SudokuUniquenessError(Exception):
    pass

class SudokuValueError(Exception):
    pass 

class SudokuIndexError(Exception):
    pass

class Board(object):

    def __init__(self, start_board=None): #start_board should be a 9x9 array with 0 as a placeholder
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self.cols = [Column(i) for i in range(9)]
        self.rows = [Row(i) for i in range(9)]
        self.boxes = [[Box(i, j) for i in range(3)] for j in range(3)]

        if start_board is not None: #Could refactor this probably. 
            for x in range(9):
                for y in range(9):
                    n = start_board[x][y]
                    if n != 0:
                        self.add_number(n, x, y)


    def print_board(self):
        print('-'*19)
        rownum = 0
        for _ in range(3):
            for _ in range(3):
                subrows = [' '.join(map(str, self.grid[rownum][3*i:3*i+3])) \
                        for i in range(3)]
                print('|' + '|'.join(subrows) + '|')
                rownum += 1 

            print('-'*19)


    def add_number(self, num, row, col):
     
        if num not in range(1,10):
            raise SudokuValueError
        elif row not in range(9) or col not in range(9):
            raise SudokuIndexError
        else:
            self.grid[row][col] = num
            self.cols[col].add(num)
            self.rows[row].add(num)
            self.boxes[row//3][col//3].add(num)

    def remove_number(self, row, col):
        num = self.grid[row][col]
        if num != 0:#throw excpetion if it's already 0?
            self.cols[col].remove(num)
            self.rows[row].remove(num)
            self.boxes[row//3][col//3].remove(num)
            self.grid[row][col] = 0
        return num # I like the idea of returning it like pop 

    def valid_play(self, num, row, col):
        return self.cols[col].free(num) and self.row[row].free(num) \
                and self.boxes[row//3][col//3].free(num)

    def deem_impossible(self, num, row, col):
        self.possible[row][col].remove(num)


class Unit(object):
    def __init__(self, ind, start_nums):
        self.nums = set(start_nums)
        self.index = ind

    def free(self, num):
        return num not in self.nums

    def add(self, num):
        if num in self.nums:
            raise SudokuUniquenessError("{} not unique".format(num)) 
        else:
            self.nums.add(num)

    def remove(self, num):
        self.nums.remove(num)

class Box(Unit):

    def __init__(self, boxrow, boxcol, start_nums=[]):
        super().__init__((boxrow, boxcol), start_nums)

#    def __repr__(self):
 #       return "Box {} containing {}".format(self.index, self.nums)

class Row(Unit):
    
    def __init__(self, rownum, start_nums=[]):
        super().__init__(rownum, start_nums)

  #  def __repr__(self):
   #     return "Row {}".format(self.index, self.nums)

class Column(Unit):

    def __init__(self, colnum, start_nums=[]):
        super().__init__(colnum, start_nums)

 #   def __repr__(self):
  #      return "Column {} containing {}".format(self.nums)

"""Questions/Thoughts:
    - Should I make my own error for when a number does not work?
    - Start with user solving, add AI later
    - How exactly does inheritance work?
    - Put in safeguards to make sure the indexy attributes are in the correct range (0 to 8 or 1 to 9...?)
    - Do this in Python 3?
    - Refactor where type is just a member of unit? Really they are the same. maybe I'll went different print methods though
    - Generate my own sudoku boards?
    - I could keep a 9x9 simple list to hold the numbers... or I could rely on Column and Row being implemented 
      correctly, and just use one of them. Let's start with
    - A little silly to have the index be a member... but it would be nice to be able to distinguish them by more than their index in the arrays. """






