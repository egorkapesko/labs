def count_words(sentence):
    """
    Функция для подсчета слов в предложении.
    """
    if not sentence or sentence.isspace():
        return 0
    
    words = sentence.split()
    return len(words)