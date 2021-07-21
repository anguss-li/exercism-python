SCORES = {
    **{letter: 1 for letter in "AEIOULNRST"},
    **{letter: 2 for letter in "DG"},
    **{letter: 3 for letter in "BCMP"},
    **{letter: 4 for letter in "FHVWY"},
    **{letter: 5 for letter in "K"},
    **{letter: 8 for letter in "JX"},
    **{letter: 10 for letter in "QZ"},
}


def score(word: str) -> int:
    '''Return the total scrabble score of word'''
    return sum([SCORES[letters]
                for letters in SCORES
                for letter in word.upper()
                if letter in letters])
