from re import sub
from string import ascii_lowercase

ALPHABET = set(ascii_lowercase)


def is_pangram(sentence: str) -> bool:
    '''
    sentence: string, phrase to be tested
    returns: True if sentence is a pangram, otherwise False
    '''
    return set(sub(r'[^a-z]', '', sentence.lower())) == ALPHABET
