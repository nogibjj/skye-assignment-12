from src.dotp import dot_product


def test_dot_product():
    assert dot_product([1, 2, 3], [1, 2, 3]) == 14
    assert dot_product([],[]) == 0

