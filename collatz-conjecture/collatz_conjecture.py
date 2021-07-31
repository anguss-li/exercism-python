def steps(number: int) -> int:
    '''
    Count the steps needed to reach 1 using the method in the Collatz Conjecture
    '''
    if number <= 0:
        raise ValueError("Integer must be strictly positive.")
    step = 0
    while number != 1:
        number = number/2 if number % 2 == 0 else number*3 + 1
        step += 1
    return step
