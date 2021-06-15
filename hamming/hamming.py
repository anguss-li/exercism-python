def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(1 for char_a, char_b in zip(strand_a, strand_b) if char_a != char_b)
