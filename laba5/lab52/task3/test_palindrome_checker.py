import pytest
from palindrome_checker import is_palindrome

def test_simple_palindromes():
    assert is_palindrome("радар") == True
    assert is_palindrome("топот") == True

def test_simple_non_palindromes():
    assert is_palindrome("привет") == False
    assert is_palindrome("мир") == False

def test_numbers():
    assert is_palindrome(12321) == True
    assert is_palindrome(12345) == False

def test_case_insensitive():
    assert is_palindrome("Анна") == True
    assert is_palindrome("АнНа") == True

def test_with_spaces():
    assert is_palindrome("а роза упала на лапу азора") == True

def test_edge_cases():
    assert is_palindrome("") == True
    assert is_palindrome("а") == True
    assert is_palindrome(1) == True