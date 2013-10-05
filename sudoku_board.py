#I have this idea to start a sudoku solver. I think we want a board to start.
#For consistency, everything with be 1 index
#Some other design thoughts -

class SudokuUniquenessError(Exception):
    pass

class SudokuValueError(Exception):
    pass 

class SudokuIndexError(Exception):
    pass

class SudokuNonRemovableError(Exception):
    pass

class Board(object):
    #TODO: refactor to access grid using 1 indexing. 
    def __init__(self, start_board=None): #start_board should be a 9x9 array with 0 as a placeholder
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self.removable = [[True for _ in range(9)] for _ in range(9)]
        self.cols = [Column(i) for i in range(1, 10)]
        self.rows = [Row(i) for i in range(1, 10)]
        self.boxes = [[Box(i, j) for i in range(1,4)] for j in range(1,4)]

        if start_board is not None: #Could refactor this probably. 
            for x in range(9):
                for y in range(9):
                    n = start_board[x][y]
                    if n != 0:
                        self.add_number(n, x+1, y+1)
                        self.removable[x][y] = False

    def num_at(self, row_label, col_label):
        row = row_label - 1
        col = col_label - 1
        return self.grid[row][col]


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


    def add_number(self, num, row_label, col_label):
        row = row_label - 1
        col = col_label - 1

        if num not in range(1,10):
            raise SudokuValueError
        elif row not in range(9) or col not in range(9):
            raise SudokuIndexError
        elif self.grid[row][col]!=0:
            raise SudokuUniquenessError('Space ({},{}) is already occupied'.format(row_label, col_label))
        else:
            self.grid[row][col] = num
            self.cols[col].add(num)
            self.rows[row].add(num)
            self.boxes[row//3][col//3].add(num)

    def remove_number(self, row_label, col_label):
        '''Should I be able to do this? Shouldn't it be stuck forever?'''
        row = row_label - 1
        col = col_label - 1

        if self.removable[row][col]:
            num = self.grid[row][col]
            if num != 0:#throw excpetion if it's already 0?
                self.cols[col].remove(num)
                self.rows[row].remove(num)
                self.boxes[row//3][col//3].remove(num)
                self.grid[row][col] = 0
            return num # I like the idea of returning it like pop 
        else:
            raise SudokuNonRemovableError

    def valid_play(self, num, row_label, col_label):
        row = row_label - 1
        col = col_label - 1

        return self.cols[col].free(num) and self.rows[row].free(num) \
                and self.boxes[row//3][col//3].free(num) \
                and self.cell_open(row_label, col_label)

    def cell_open(self, row_label, col_label):
        return self.grid[row_label-1][col_label-1] == 0

    def is_solved(self):
        #Sort of brutish way of doing this:
        for row in self.grid:
            if 0 in row:
                return False
        return True

class Unit(object):
    def __init__(self, ind=0, start_nums=[]): #Should I add a safety here too?
        self.nums = set(start_nums)
        self.index = ind

    def free(self, num):
        return num not in self.nums

    def add(self, num):
        if num in self.nums:
            raise SudokuUniquenessError 
        else:
            self.nums.add(num)

    def remove(self, num):
        self.nums.remove(num)

    def remaining(self):
        return set(range(1,10)).difference(self.nums)

class Box(Unit):

    def __init__(self, boxrow, boxcol, start_nums=[]):
        super().__init__((boxrow, boxcol), start_nums)

    def add(self, num):
        try:
            super().add(num)
        except SudokuUniquenessError:
            raise SudokuUniquenessError('Box {} already contains {}'.format(self.index, num))
    

class Row(Unit):
    
    def __init__(self, rownum, start_nums=[]):
        super().__init__(rownum, start_nums)

    def add(self, num):
        try:
            super().add(num)
        except SudokuUniquenessError as e:
            raise SudokuUniquenessError('Row {} already contains {}'.format(self.index, num))


class Column(Unit):

    def __init__(self, colnum, start_nums=[]):
        super().__init__(colnum, start_nums)

    def add(self, num):
        try:
            super().add(num)
        except SudokuUniquenessError as e:
            raise SudokuUniquenessError('Column {} already contains {}'.format(self.index, num))


"""Questions/Thoughts:
    - Refactor where type is just a member of unit? Really they are the same. maybe I'll went different print methods though
    - Generate my own sudoku boards?
    - I could keep a 9x9 simple list to hold the numbers... or I could rely on Column and Row being implemented 
      correctly, and just use one of them. Let's start with
    - A little silly to have the index be a member... but it would be nice to be able to distinguish them by more than their index in the arrays. 
    - By one argument, the possibilities should be factored into the AI, the board itself should only add, remove, and check for validity. 
    - Do I want the board to _play_... no i think the player should play ?
    - Pay more attention to where I throw exceptions...
    - Check that starter board is valid"""

