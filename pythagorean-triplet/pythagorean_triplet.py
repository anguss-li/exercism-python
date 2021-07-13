from math import sqrt
from typing import List


def triplets_with_sum(number: int) -> List[List[int]]:
    '''Return all pythagorean triplets which sum to number'''
    # a**2 + b**2 = c**2, a + b + c = N
    # a + b = N - c
    # Solving system of equations for a and b:
    # let D = sqrt(c**2 - N**2 + 2*N*c)
    # a = (N-c-D) / 2
    # b = (N-c+D) / 2
    # D is real for c > N * (sqrt(2) - 1)
    # And c < N/2 from the problem statement
    triplets = []
    for c in range(number//2 - 1, int((sqrt(2)-1) * number), -1):
        D = sqrt(c**2 - number**2 + 2*number*c)
        if D.is_integer():
            triplets.append([(number-c-D) / 2, (number-c+D) / 2, c])
    return triplets
