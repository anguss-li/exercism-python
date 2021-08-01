from math import prod


def largest_product(series: str, size: int) -> int:
    '''Find largest product of a substring of digits in series of given size.'''
    if size < 0:
        raise ValueError('Size must be positive.')
    elif size > (length := len(series)):
        raise ValueError('Size cannot be larger than series.')
    elif length == 0 or size == 0:
        return 1

    return max(prod(int(series[i+n]) for n in range(size))
               for i in range(length-size+1))
