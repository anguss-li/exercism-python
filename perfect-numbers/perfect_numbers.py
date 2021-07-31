def classify(number):
    '''
    number: integer, number to be classified
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
        factors = {0}

        for i in range(1, int(number ** 0.5)+1):
            if number % i == 0:
                factors.update((i, number//i))
        factors.remove(number)

        return sum(factors)

    factors_sum = aliquot_sum(number)

    if factors_sum == number:
        return "perfect"
    elif factors_sum > number:
        return "abundant"
    elif factors_sum < number:
        return "deficient"
