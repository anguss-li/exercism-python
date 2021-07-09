from string import ascii_lowercase


def is_isogram(string: str) -> bool:
    '''Check if all letters in string are unrepeated'''
    word = string.lower()
    return not any(word.count(char) > 1 and char in ascii_lowercase for char in word)
