def is_palindrome(input_value):

    text = str(input_value)

    text = text.replace(" ", "").lower()

    return text == text[::-1]