import pytest
from find_max import find_max


def test_positive_numbers():
    assert find_max([1, 5, 3, 10, 2]) == 10


def test_negative_numbers():
    assert find_max([-10, -3, -50, -1]) == -1


def test_single_element():
    assert find_max([42]) == 42


def test_empty_list():
    with pytest.raises(ValueError):
        find_max([])
git add test_find_max.py
git commit -m "Добавлены тесты для функции find_max"
