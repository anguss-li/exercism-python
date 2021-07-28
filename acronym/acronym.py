from re import findall


def abbreviate(words: str) -> str:
    '''Returns acronym in capital letters of sentence.'''
    return ''.join(word[0].upper() for word in findall(r"[a-zA-Z']+", words))
