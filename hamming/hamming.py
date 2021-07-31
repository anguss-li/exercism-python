def distance(strand_a: str, strand_b: str) -> int:
    '''Count the number of differing characters between the two strands.'''
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be of equal length.')
    return sum(1 for a, b in zip(strand_a, strand_b) if a != b)
