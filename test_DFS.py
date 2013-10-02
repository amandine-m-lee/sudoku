import pytest
from sudoku_AI import *
from sudoku_board import *

@pytest.fixture
def dfs():
    from sample_boards import b1
    return DFSPlayer(b1)

def test_init(dfs):
    assert dfs.cur_row == 1
    assert dfs.cur_col == 1
    assert len(dfs.open_cells) == 46

def test_increment_decrement(dfs):
    assert dfs.cell_index == 0
    dfs.increment_coord()
    assert dfs.cell_index == 1
    assert dfs.cur_row == 1
    assert dfs.cur_col == 2
    dfs.increment_coord()
    assert dfs.cell_index == 2
    assert dfs.cur_row == 1
    assert dfs.cur_col == 4
    dfs.decrement_coord()
    assert dfs.cell_index == 1
    assert dfs.cur_row == 1
    assert dfs.cur_col == 2

def test_poss():
    from sample_boards import b1
    p = DFSPlayer.poss(None,8,1,b1)
    assert next(p) == 9
    with pytest.raises(StopIteration):
        next(p)
    p1 = DFSPlayer.poss(None,8,1,b1)
    b1.add_number(9,1,1)
    with pytest.raises(StopIteration):
        next(p1)
   

