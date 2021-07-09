from typing import List, Tuple


def get_products(lower: int, upper: int) -> List[int]:
    '''Return all possible products of integers between the factors'''
    initial_range = range(lower, upper + 1)
    return [x * i for x in initial_range for i in initial_range]


def get_palindromes(products: List[int]) -> List[int]:
    ''''''

    def is_palindrome(n: int) -> bool:
        '''Check if number remains the same when its digits are reversed'''
        n_copy = n
        reverse = 0
        while n_copy > 0:
            last_digit = n_copy % 10
            reverse = (reverse * 10) + last_digit
            n_copy //= 10
        return n == reverse

    return [x for x in products if is_palindrome(x)]


def get_factors(n: int, min_factor: int, max_factor: int) -> List[List[int]]:
    '''Return all factors of number within the limit'''
    if n == None:
        return []
    root = int(n ** 0.5)
    lower = min_factor if min_factor > n // max_factor else n // max_factor
    upper = (max_factor if max_factor < root else root) + 1
    return [[i, n // i] for i in range(lower, upper) if n % i == 0]


def largest(min_factor: int, max_factor: int) -> Tuple[int, List[List[int]]]:
    '''
    Return the largest palindromic number in the range between min_factor and 
    max_factor (both inclusive) as well as said number's factors
    '''
    if min_factor > max_factor:
        raise ValueError("Minimum factor is larger than maximum factor.")

    palindromes = get_palindromes(get_products(min_factor, max_factor))
    largest = max(palindromes, default=None)
    return largest, get_factors(largest, min_factor, max_factor)


def smallest(min_factor: int, max_factor: int) -> Tuple[int, List[List[int]]]:
    '''
    Return the smallest palindromic number in the range between min_factor and 
    max_factor (both inclusive) as well as said number's factors
    '''
    if min_factor > max_factor:
        raise ValueError("Minimum factor is larger than maximum factor.")

    palindromes = get_palindromes(get_products(min_factor, max_factor))
    smallest = min(palindromes, default=None)
    return smallest, get_factors(smallest, min_factor, max_factor)
