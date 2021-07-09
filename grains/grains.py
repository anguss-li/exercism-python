def square(number: int) -> int:
    '''Calculate the number of grains on any given chessboard square'''
    if not 1 <= number <= 64:
        raise ValueError("Invalid index for a chessboard square")
    return 2 ** (number - 1)


def total() -> 18446744073709551615:
    '''Return the total number of grains on the chessboard'''
    return 18446744073709551615
