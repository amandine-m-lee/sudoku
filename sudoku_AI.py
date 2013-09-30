class Player(object):

    def __init__(self, board):
        self.board = board

        self.possible = [[set(range(1,10)) for _ in range(9)] for _ in range(9)]

    def deem_impossible(self, num, row_label, col_label):
        row = row_label - 1
        col = col_label - 1

        self.possible[row][col].remove(num)

'''Thoughts here:
    - Pass it a board object? Or something else? 

    
