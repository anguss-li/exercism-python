from typing import List

SPACER = ', '


def recite(start: int, take: int = 1) -> List[str]:
    '''
    Recite the Beer Song.

    Parameters:
        start: starting number of beer bottles
        take: number of verses to be recited after start (max 100)
    '''
    verses = []

    def bottles(n: int, is_refrain: bool = False) -> str:
        '''State the number of beer bottles on the wall.'''
        number = 99 if n == -1 else n if n else 'no more'
        is_plural = 's' if n != 1 else ''
        ending = ' on the wall' if not is_refrain else '.'
        return f'{number} bottle{is_plural} of beer' + ending

    def taken(n: int) -> str:
        '''State how many beer bottles should be taken off the wall.'''
        if n > 0:
            singular = 'one' if n > 1 else 'it'
            return f'Take {singular} down and pass it around'
        else:
            return 'Go to the store and buy some more'

    for n in range(start, (end := start-take), -1):
        verses.append(bottles(n).capitalize() + SPACER + bottles(n, True))
        verses.append(taken(n) + SPACER + bottles(n-1) + '.')
        if n > end+1:
            verses.append('')
    return verses
