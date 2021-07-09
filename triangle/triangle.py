from typing import List


def inequality(sides: List[int]) -> bool:
    '''
    Check if the triangle inequality, i.e. that the sum of any two sides is 
    greater than or equal to the remaining third side, is fulfilled
    '''
    smallest, middle, largest = sorted(sides)
    return smallest + middle >= largest and all(s > 0 for s in sides)


def equilateral(sides: List[int]) -> bool:
    '''Check if all sides are equal'''
    a, b, c = sides
    return a == b == c and inequality(sides)


def isosceles(sides: List[int]) -> bool:
    '''Check if only two sides are equal'''
    return any(sides.count(x) > 1 for x in sides) and inequality(sides)


def scalene(sides: List[int]) -> bool:
    '''Check if no sides are equal'''
    a, b, c = sides
    return a != b != c and inequality(sides)
