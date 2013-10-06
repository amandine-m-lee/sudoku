from sudoku_AI import *
import pytest

@pytest.fixture
def smarter():
    from sample_boards import b1
    return SmarterPlayer(b1)

def test_matematching(): #NOTE: you can use the individual functions from a class separately, I would assume
#how do you deal with passing in self?
    first = SmarterPlayer.get_rowmates(0,0)
    first.sort()
    assert first == [(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8)]
    second = SmarterPlayer.get_colmates(3,3)
    second.sort()
    assert second == [(0,3),(1,3),(2,3),(4,3),(5,3),(6,3),(7,3),(8,3)]
    third = SmarterPlayer.get_boxmates(5,2)
    third.sort()
    z = [(3,0),(4,0),(5,0),(4,1),(5,1),(3,1),(4,2),(5,2),(3,2)]
    z.sort()
    assert third == z 



