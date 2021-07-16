from typing import List


def primes(limit: int) -> List[int]:
    '''Find all primes from 2 to limit using the Sieve of Eratosthenes'''
    is_marked = [False] * (limit+1)
    numbers = range(2, limit+1)
    for number in numbers:
        if not is_marked[number]:
            for i in range(number**2, limit+1, number):
                is_marked[i] = True
    return [number for number in numbers if not is_marked[number]]