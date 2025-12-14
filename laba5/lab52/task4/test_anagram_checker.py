import pytest
from anagram_checker import are_anagrams

def test_basic_anagrams():
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("triangle", "integral") == True

def test_basic_non_anagrams():
    assert are_anagrams("hello", "world") == False
    assert are_anagrams("python", "java") == False

def test_different_lengths():
    assert are_anagrams("abc", "abcd") == False
    assert are_anagrams("a", "ab") == False

def test_case_insensitive():
    assert are_anagrams("Listen", "Silent") == True
    assert are_anagrams("ABC", "cba") == True

def test_with_spaces():
    assert are_anagrams("school master", "the classroom") == True
    assert are_anagrams("debit card", "bad credit") == True

def test_empty_strings():
    assert are_anagrams("", "") == True
    assert are_anagrams("", "a") == False

def test_numbers_in_strings():
    assert are_anagrams("123", "321") == True
    assert are_anagrams("a1b2", "2b1a") == True