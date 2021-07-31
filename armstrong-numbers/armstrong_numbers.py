def is_armstrong_number(number: int) -> bool:
    '''Check if the given number is a narcissistic/Armstrong number.'''
    digits = str(number)
    length = len(digits)
    return sum(int(digit) ** length for digit in digits) == number
