from sudoku_board import *

class BoardSolved(Exception):
    pass
class NoSolutions(Exception):
    pass

class DFSPlayer(object):
    
    def __init__(self, board):
        self.board = board
        self.plays = [] #This can actually act like a log now
        self.cur_row = 1
        self.cur_col = 1
        self.tracker = [self.poss(1,1)] #our stack of generators!

    def next_play(self):
    
        try:
            num = next(self.tracker[-1])
            self.board.add(num, self.cur_row, self.cur_col)
            self.plays.append((num, self.cur_row, self.cur_col))
            self.increment_coord()
            self.tracker.append(self.poss(self.cur_row, self.cur_col))
            
        except StopIteration:
            self.tracker.pop()
            self.decrement_coord()
            self.board.remove(self.cur_row, self.cur_col)
            self.next_play()

    def solve_board():
        while(True):
            try:
                self.next_play()
            except BoardSolved:
                print("BOARD IS SOLVED")
                self.board.print_board()
                break
            except NoSolutions:
                print("BOARD NOT SOLVABLE :(")
                break

    def increment_coord(self): #This might be better refactored as a list with an index that scrolls back and forth. 
        if self.cur_col < 10:
            self.cur_col += 1
        else:
            if self.cur_row < 10:
                self.cur_col = 1
                self.cur_row += 1
            else:
                raise BoardSolved
        if not self.board.removable(self.cur_row - 1, self.cur_col -1):
            self.increment_coord()#Should probably return or something here
    
    def decrement_coord(self):
        if self.cur_col != 1:
            self.cur_col -= 1
        else:
            if self.cur_row == 1:
                raise NoSolutions
            else:
                self.cur_row -= 1
                self.cur_col = 9
        if not self.board.removable(self.cur_row - 1, self.cur_col -1):
            self.decrement_coord() 
            
    def poss(self, row, col): # A generator. Will i run into problems as i mutate stae?
        for i in range(1,10):
            if self.board.valid_play(i, row, col):
                yield i

    #If it does't have nxt, then wahta/ 

if __name__ == '__main__':
    from sample_boards import b1

    pl = DFSPlayer(b1)


        

'''Thoughts here:
    - Pass it a board object? Or something else?
    - Ideas I had - trigger pairs. 
    - Go methodically through and
    - I like the idea of doing this as not so much procedural as functional programming. It would actually be really useful.
    
    TACTICS:
    - Look for
    - Iterate back and forth between updating possibles and assigning values.
    - What if I kept the board in python and then accessed it in Haskell or soemthing to write the functional implementation?'''



   
