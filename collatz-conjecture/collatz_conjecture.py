def steps(number: int) -> int:
    '''
    Count the steps needed to reach 1 using the method in the Collatz Conjecture
    '''
    if number <= 0:
        raise ValueError("Integer must be strictly positive.")
    n = number
    step = 0
    while n != 1:
        n = n / 2 if n % 2 == 0 else n * 3 + 1
        step += 1
    return step
