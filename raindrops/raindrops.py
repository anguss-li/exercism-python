def convert(number):
    '''
    number: integer, number which will be 'converted' into raindrop sounds
    returns: string, see README
    '''
    converted_number = ''
    factors = {3:'i', 5:'a', 7:'o'}
    for factor in factors:
        if number % factor == 0:
            converted_number += ('Pl' + factors[factor] + 'ng')
    if len(converted_number) == 0:
        converted_number = str(number)
    return converted_number