def is_armstrong_number(number):
    '''
    number: int, number to be tested for narcissism
    returns: True if number is a narcissistic/Armstrong number, False otherwise
    '''
    digits = str(number)
    digits_num = len(digits)
    return sum(int(digit) ** digits_num for digit in digits) == number