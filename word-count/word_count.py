from re import compile, sub
from typing import Dict


def count_words(sentence: str) -> Dict[str, int]:
    '''Return all words in sentence as well as their frequency'''
    is_word = compile(r"(?:\w[']\w|\w)+")
    words = is_word.findall(sub(r"[,.;_@#?!&$]+", " ", sentence).lower())
    return {word: words.count(word) for word in words}
