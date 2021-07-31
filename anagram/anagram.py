from typing import List


def find_anagrams(word: str, candidates: List[str]) -> List[str]:
    '''Return all candidate words that are anagrams of the given word.'''
    word = word.lower()
    letters = sorted(word)
    return [candidate 
            for candidate in candidates
            if sorted((reference := candidate.lower())) == letters
            and reference != word]
