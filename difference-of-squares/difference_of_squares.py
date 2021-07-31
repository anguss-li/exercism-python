def square_of_sum(number: int) -> int:
    '''Square the sum of the natural numbers up to the number given.'''
    return ((number*(number+1))/2) ** 2


def sum_of_squares(number: int) -> int:
    '''Sum the squares of the natural numbers up to the number given.'''
    return (number*(number+1)*(2*number+1)) / 6


def difference_of_squares(number: int) -> int:
    '''Subtract the sum of squares for number given by the square of its sum.'''
    return square_of_sum(number) - sum_of_squares(number)
