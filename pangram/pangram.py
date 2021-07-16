from re import sub
from string import ascii_lowercase

ALPHABET = set(ascii_lowercase)


def is_pangram(sentence: str) -> bool:
    '''
    Check if sentence contains all letters in the alphabet at least once
    '''
    return set(sub(r'[^a-z]', '', sentence.lower())) == ALPHABET
