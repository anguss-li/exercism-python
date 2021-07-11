from typing import List


def sum_of_multiples(limit: int, numbers: List[int]) -> int:
    '''
    Find the sum of all multiples in numbers in the range between 0 and limit-1.
    '''
    return sum({multiple 
                for number in numbers if number != 0 
                for multiple in range(number, limit, number)})