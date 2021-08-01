FACTORS = [(3, 'Pling'), (5, 'Plang'), (7, 'Plong')]


def convert(number: int) -> str:
    '''Convert number into raindrop sounds.'''
    converted = ''.join(factor[1]
                        for factor in FACTORS
                        if number % factor[0] == 0)
    return converted if converted else str(number)
