import word_count

def test_basic():
    assert word_count.count_words("Hello world") == 2

def test_empty():
    assert word_count.count_words("") == 0

def test_spaces():
    assert word_count.count_words("   ") == 0

def test_multiple_spaces():
    assert word_count.count_words("Multiple   spaces") == 2

def test_single_word():
    assert word_count.count_words("Hello") == 1