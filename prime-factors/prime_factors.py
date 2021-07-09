from typing import List


def factors(value: int) -> List[int]:
    '''Find the prime factors which can be multiplied to produce value'''
    value_copy = value
    factors = []
    for number in range(2, value + 1):
        while value_copy % number == 0:
            value_copy //= number
            factors.append(number)
        if value_copy == 1:
            break
    return factors
