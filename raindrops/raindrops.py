def convert(number):
    '''
    number: integer, number which will be 'converted' into raindrop sounds
    returns: string, see README
    '''
    converted_number = ''
    factors = [(3, 'Pling'), (5, 'Plang'), (7, 'Plong')]
    for factor in factors:
        if number % factor[0] == 0:
            converted_number += factor[1]
    return converted_number if len(converted_number) != 0 else str(number)