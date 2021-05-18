import string


def is_valid(isbn):
    isbn_digits = isbn.replace("-", "")
    if len(isbn_digits) != 10:
        return False
    digit_sum = 0
    for index in range(len(isbn_digits)):
        digit = isbn_digits[index]
        if digit == "X" and index == 9:
            to_add = 10 * (10 - index)
        elif digit not in string.digits:
            return False
        else:
            to_add = int(digit) * (10 - index)
        digit_sum += to_add
    return digit_sum % 11 == 0
