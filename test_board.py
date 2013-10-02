from sudoku_board import *
import pytest

def test_unit():
    u = Unit()
    u.add(4)
    assert 4 in u.nums
    u.remove(4)
    assert 4 not in u.nums
    u1 = Unit(1,[5,4,3])
    u1.add(6)
    with pytest.raises(SudokuUniquenessError):
        u1.add(3)
    assert u1.remaining() == set([1,2,7,8,9]) #Make more flexible - any size set?
        
def test_column():
    pass


@pytest.fixture
def sb():
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

def test_add_number(sb): #if you think about it, these test aren't really naive to my implementation... 
    sb.add_number(7,9,5)
    assert sb.grid[8][4] == 7
    assert 7 in sb.cols[8].nums
    assert 7 in sb.rows[4].nums
    assert 7 in sb.boxes[2][1].nums

def test_add_number_exceptions(sb):
    with pytest.raises(SudokuIndexError):
        sb.add_number(4,10,2)
    with pytest.raises(SudokuValueError):
        sb.add_number(-5,3,4)
    with pytest.raises(SudokuUniquenessError):
        sb.add_number(4,1,2)#The box
    with pytest.raises(SudokuUniquenessError):
        sb.add_number(3,1,1) #The column
    with pytest.raises(SudokuUniquenessError):
        sb.add_number(5,1,1)

def test_remove_number(sb):
    sb.add_number(1,1,1)
    assert sb.remove_number(1,1) == 1
    assert sb.grid[1][1] == 0
    assert 1 not in sb.cols[0].nums
    assert 1 not in sb.rows[0].nums
    assert 1 not in sb.boxes[0][0].nums
    with pytest.raises(SudokuNonRemovableError):
        sb.remove_number(2,1)
    
def test_valid_play(sb):
    assert sb.valid_play(1,1,1)
    assert not sb.valid_play(3,1,1)

def test_is_solved(sb):
    assert not sb.is_solved()
    b = Board([[0,2,7,1,5,4,3,9,6],
               [9,6,5,3,2,7,1,4,8],
               [3,4,1,6,8,9,7,5,2],
               [5,9,3,4,6,8,2,7,1],
               [4,7,2,5,1,3,6,8,9],
               [6,1,8,9,7,2,4,3,5],
               [7,8,6,2,3,5,9,1,4],
               [1,5,4,7,9,6,8,2,3],
               [2,3,9,8,4,1,5,6,7]])
    b.add_number(8,1,1)
    assert b.is_solved()
 
