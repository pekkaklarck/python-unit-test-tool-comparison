from sut import compare


def test_x_greater_than_y_returns_1():
    for x, y in [(2, 1), (1, 0), (0, -1), (1.1, 1)]:
        assert compare(x, y) == 1

def test_x_equal_to_y_returns_0():
    for x in [0, 1, -1, 1.1]:
        assert compare(x, x) == 0

def test_x_less_than_y_returns_minus_1():
    for x, y in [(1, 2), (0, 1), (-1, 0), (1, 1.1)]:
        assert compare(x, y) == -1

def test_failing():
    assert compare(1, 0) == 0
