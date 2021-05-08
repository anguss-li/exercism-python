def is_armstrong_number(number):
    '''
    number: int, number to be tested for narcissism
    returns: True if number is a narcissistic/Armstrong number, False otherwise
    '''
    powered_sum = 0
    digits = str(number)
    digits_len = len(digits)
    for digit in digits:
        powered_sum += int(digit) ** digits_len
    return powered_sum == number
