from string import digits


def is_valid(isbn: str) -> bool:
    '''Verify a ISBN-10 number.'''
    number = list(isbn.replace('-', ''))
    if len(number) != 10:
        return False
    digit_sum = 0
    for index, digit in enumerate(number):
        if index == 9 and digit == 'X':
            value = 10
        elif digit not in digits:
            return False
        else:
            value = int(digit)
        digit_sum += value * (10-index)
    return digit_sum % 11 == 0
