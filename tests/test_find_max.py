import pytest
from find_max import find_max


def test_find_max_positive_numbers():
    assert find_max([1, 3, 2]) == 3


def test_find_max_other_positive_numbers():
    assert find_max([5, 1, 4]) == 5


def test_find_max_single_element():
    assert find_max([42]) == 42


def test_find_max_negative_numbers():
    assert find_max([-10, -3, -7]) == -3


def test_find_max_empty_list():
    with pytest.raises(ValueError):
        find_max([])
