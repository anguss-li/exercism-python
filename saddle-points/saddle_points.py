from typing import List, Dict


def saddle_points(matrix: list) -> List[Dict[str, int]]:
    '''
    Return all entries which are largest in their row and are smallest in their
    column.
    '''
    if len(set(map(len, matrix))) > 1:
        raise ValueError("Rows must all be of equal length.")

    points = set()

    for i, row in enumerate(matrix):
        for j, x in enumerate(row):
            if x == max(row) and x == min([row[j] for row in matrix]):
                points.add((i + 1, j + 1))

    return [{"row": point[0], "column": point[1]} for point in points]
