from sudoku_board import *
import pytest

def test_unit():
    pass
def test_column():
    pass


@pytest.fixture
def sample_board():
    array = [[0,0,3,0,0,0,0,2,5],
             [4,0,0,0,9,0,0,7,0],
             [6,0,8,7,0,5,9,0,3],
             [8,6,0,0,1,7,0,0,0],
             [2,0,0,0,3,0,0,0,7],
             [0,0,0,9,2,0,0,6,4],
             [3,0,1,4,0,9,7,0,2],
             [0,7,0,0,5,0,0,0,8],
             [5,4,0,0,0,0,6,0,0]]

    return Board(array)

def test_board(sample_board):
    sample_board.add(1,2,1)
    
