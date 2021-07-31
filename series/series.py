from typing import List


def slices(series: str, length: int) -> List[str]:
    '''Slice series of digits into subsections of set length'''
    if length > (digits := len(series)) or length < 1:
        raise ValueError(f'Cannot slice {digits} digits using {length} length')

    return [''.join(series[i:i+length]) for i in range(digits-length+1)]
