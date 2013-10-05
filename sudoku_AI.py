from sudoku_board import *

class BoardSolved(Exception):
    pass
class NoSolutions(Exception):
    pass

class DFSPlayer(object):
    
    def __init__(self, board):
        self.board = board
        self.plays = [] #A log of steps
        self.open_cells = self.get_open_cells(self.board)
        self.cell_index = 0
        self.cur_row, self.cur_col = self.open_cells[0]
        self.tracker = [self.poss(self.cur_row, self.cur_col, self.board)]

    def next_play(self):
        self.board.print_board()   
        for num in (self.tracker[-1]):
            self.board.add_number(num, self.cur_row, self.cur_col)
            self.plays.append((num, self.cur_row, self.cur_col))
            self.increment_coord()
            self.tracker.append(self.poss(self.cur_row, self.cur_col, self.board))
            return num 

        else:
            self.tracker.pop()
            self.decrement_coord()
            self.board.remove_number(self.cur_row, self.cur_col)
            self.next_play()

    def solve_board(self):
        while(True):
            try:
                self.next_play()
            except BoardSolved:
                print("BOARD IS SOLVED in {} steps".format(len(self.plays)))
                self.board.print_board()
                break
            except NoSolutions:
                print("BOARD NOT SOLVABLE :( tried {} steps".format(len(self.plays)))
                break

    def increment_coord(self): #This might be better refactored as a list with an index that scrolls back and forth. 
        self.cell_index += 1
        try:
            self.cur_row, self.cur_col = self.open_cells[self.cell_index]
        except IndexError:
            raise BoardSolved

    def decrement_coord(self):
        self.cell_index -= 1
        if self.cell_index > -1:
            self.cur_row, self.cur_col = self.open_cells[self.cell_index]
        else:
            raise NoSolutions

    def poss(self, row, col, board): # A generator that goes through every possible number
        for i in range(1,10):
            if board.valid_play(i, row, col):
                yield i

    def get_open_cells(self, board):
        ret = []
        for i in range(9):
            for j in range(9):
                if board.removable[i][j]:
                    ret.append((i+1, j+1))
        return ret

class SmarterPlayer(object):
    
    def __init__(self, b):
        self.board = b
        self.scells = [[SmartCell(b, i, j) for i in range(1,10)] \
                for j in range(1,10)]
        self.initial_dependencies() #Never sure whether to pass in members of self

#TODO: Finish the box part
    def initial_dependencies(self):
        for rindex in range(9):
            for cindex in range(9):
                rowmates = zip([rindex]*8, [n for n in range(9)].remove(cindex))
                colmates = zip([n for n in range(9)].remove(rindex), [cindex]*8)
                boxrow = rindex//3
                boxcol = cindex//3
                boxmates = zip([
                for rmate in rowmates.extend(colmates).extend(boxmates):
                    row, col = rmate
                    self.scells.dependencies.append(self.scells[row][col])
#TODO: Test how far this gets without any further strategy

#TODO: Develop further strategies. 



class SmartCell(object):

    def __init__(self, b, row, col):
        self.board = b
        self.row = row
        self.col = col
        self.possibilities = [i in range(1,10)]
        self.dependencies = []

    def remove_poss(self, num):
        if num not in range(1,10):
            raise SudokuValueError
        else:
            if num in self.possibilities:
                self.possibilities.remove(num)
            if len(self.possibilities == 1):
                last = self.possibilities[0]
                self.board.add_number(last, row, col)
                for dep in self.dependencies:
                    dep.remove_poss(last)



if __name__ == '__main__':
    from sample_boards import *
    from sys import argv
     
    if len(argv) == 1:
        pl = DFSPlayer(b1)
    else:
        pl = DFSPlayer(eval(argv[1]))
    pl.solve_board()
   
