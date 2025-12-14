import pytest
from dict_merger import merge_dicts

def test_simple_merge():
    dict_a = {'a': 1, 'b': 2}
    dict_b = {'c': 3, 'd': 4}
    result = merge_dicts(dict_a, dict_b)
    assert result == {'a': 1, 'b': 2, 'c': 3, 'd': 4}

def test_overwrite_values():
    dict_a = {'a': 1, 'b': 2}
    dict_b = {'b': 20, 'c': 3}
    result = merge_dicts(dict_a, dict_b)
    assert result == {'a': 1, 'b': 20, 'c': 3}

def test_nested_dicts():
    dict_a = {'a': 1, 'nested': {'x': 10, 'y': 20}}
    dict_b = {'b': 2, 'nested': {'y': 200, 'z': 300}}
    result = merge_dicts(dict_a, dict_b)
    assert result == {'a': 1, 'b': 2, 'nested': {'x': 10, 'y': 200, 'z': 300}}

def test_empty_dicts():
    dict_a = {}
    dict_b = {'a': 1}
    result = merge_dicts(dict_a, dict_b)
    assert result == {'a': 1}

def test_dict_with_list():
    dict_a = {'a': [1, 2, 3], 'b': {'x': 10}}
    dict_b = {'a': [4, 5, 6], 'b': {'y': 20}}
    result = merge_dicts(dict_a, dict_b)
    assert result == {'a': [4, 5, 6], 'b': {'x': 10, 'y': 20}}

def test_same_dict():
    dict_a = {'a': 1, 'b': 2}
    dict_b = {'a': 1, 'b': 2}
    result = merge_dicts(dict_a, dict_b)
    assert result == {'a': 1, 'b': 2}

def test_original_dict_modified():
    dict_a = {'a': 1}
    dict_b = {'b': 2}
    original_id = id(dict_a)
    result = merge_dicts(dict_a, dict_b)
    assert id(result) == original_id