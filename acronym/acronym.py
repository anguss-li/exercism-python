def abbreviate(words: str) -> str:
    '''Returns acronym in capital letters of sentence.'''
    acronym = ''
    for word in words.upper().translate(words.maketrans('-_', '  ')).split():
        acronym += word[0]
    return acronym
