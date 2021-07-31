from typing import List


def factors(value: int) -> List[int]:
    '''Find the prime factors which can be multiplied to produce value'''
    factors = []
    for number in range(2, value+1):
        while value % number == 0:
            value //= number
            factors.append(number)
        if value == 1:
            break
    return factors
