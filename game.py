from sudoku_board import *

class Game(object):

    def __init__(self, board):
        self.board = board

    def get_move(self):
        print("Name your move (num row col)")
        move = input('>')
        num, row, col = map(int, move.split())

        try:
            self.board.add_number(num, row, col)
        except (SudokuUniquenessError, SudokuValueError, SudokuIndexError) as e:
            print(e)
            self.get_move()

    def play(self):
        solved = False
        while not solved:
            self.board.print_board()
            self.get_move()
            solved = self.board.is_solved()

        print("You solved the sudoku!!!")

if __name__ == '__main__':

    g = Game(Board([[0,0,3,0,0,0,0,2,5],
             [4,0,0,0,9,0,0,7,0],
             [6,0,8,7,0,5,9,0,3],
             [8,6,0,0,1,7,0,0,0],
             [2,0,0,0,3,0,0,0,7],
             [0,0,0,9,2,0,0,6,4],
             [3,0,1,4,0,9,7,0,2],
             [0,7,0,0,5,0,0,0,8],
             [5,4,0,0,0,0,6,0,0]]))
    g.play()

