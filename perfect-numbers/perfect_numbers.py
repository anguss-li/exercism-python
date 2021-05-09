import math


def classify(number):
    '''
    number: integer, number to be classfied
    returns: string, one of "perfect", "abundant" or "deficient" according to
    README
    '''
    if not number > 0:
        raise ValueError("Number must be a postive integer")

    def aliquot_sum(number):
        '''
        number: integer
        returns: sum of all factors of number besides itself
        '''
        if number == 1:
            return 0

        square_root = math.sqrt(number)
        factors = {1}

        for i in range(2, int(square_root) + 1):
            if number % i == 0:
                factors = factors.union([i, number // i])

        return sum(factors)

    factors_sum = aliquot_sum(number)

    if factors_sum == number:
        return "perfect"
    elif factors_sum > number:
        return "abundant"
    elif factors_sum < number:
        return "deficient"
