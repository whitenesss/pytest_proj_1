from utils import arrs
from utils import dicts

def test_get():
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 2]) == [1, 2]


def test_get_val():
    pass
