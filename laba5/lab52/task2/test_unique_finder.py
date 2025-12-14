import pytest
from unique_finder import find_unique

def test_basic_list():
    assert find_unique([1, 2, 3, 2, 4, 1, 5]) == [3, 4, 5]

def test_empty_list():
    assert find_unique([]) == []

def test_all_unique():
    assert find_unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_all_duplicates():
    assert find_unique([1, 1, 2, 2, 3, 3]) == []

def test_single_element():
    assert find_unique([42]) == [42]

def test_strings():
    assert find_unique(['a', 'b', 'a', 'c', 'd', 'b']) == ['c', 'd']

def test_mixed_types():
    assert find_unique([1, 'a', 1, 'b', 'a', 2]) == ['b', 2]

def test_none_values():
    assert find_unique([None, 1, None, 2, 3]) == [1, 2, 3]

def test_floats():
    """Тест с числами с плавающей точкой"""
    assert find_unique([1.1, 2.2, 1.1, 3.3, 4.4]) == [2.2, 3.3, 4.4]
