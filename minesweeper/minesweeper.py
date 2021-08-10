from typing import List, Tuple


def annotate(minefield: List[str]) -> List[str]:
    """Show how many adjacent mines there are to each point on the minefield."""
    if not all(len(row) == len(minefield[0]) for row in minefield):
        raise ValueError('Rows not of equal length.')
    elif any(char not in ('*', ' ') for row in minefield for char in row):
        raise ValueError('Invalid characters in minefield.')

    def count(point: Tuple[int]) -> str:
        """
        Count the number of mines adjacent to a point. If point is a mine, 
        return a mine.
        """
        if locate(point) == '*':
            return '*'

        x, y = point
        neighbours = ((x, y+1),
                      (x, y-1),
                      (x+1, y),
                      (x-1, y),
                      (x-1, y+1),
                      (x-1, y-1),
                      (x+1, y+1),
                      (x+1, y-1))

        number = sum(1
                     for neighbour in neighbours
                     if valid(neighbour)
                     and locate(neighbour) == '*')

        return str(number) if number else ' '

    def locate(point: Tuple[int]) -> str:
        """Return character at point (x, y) in the minefield."""
        return minefield[point[1]][point[0]]

    def valid(point: Tuple[int]) -> bool:
        """Check if given coordinates correspond to valid point on field"""
        return (0 <= point[0] < len(minefield[0])
                and 0 <= point[1] < len(minefield))

    return [''.join(count((x, y)) for x, _ in enumerate(row))
            for y, row in enumerate(minefield)]
