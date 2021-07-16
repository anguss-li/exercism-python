from collections import Counter
from re import findall
from typing import Dict


def count_words(sentence: str) -> Dict[str, int]:
    '''Return all words in sentence as well as their frequency'''
    return Counter(findall(r"[a-z0-9]+(?:'[a-z]+)?", sentence.lower()))
