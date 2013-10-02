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
    from sys import argv
    from sample_boards import *
    if len(argv) == 1:
        g = Game(b1)
    else:
        script, board = argv
        g = Game(eval(board))

    g.play()

