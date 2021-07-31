from typing import Dict, List


def saddle_points(matrix: List[List]) -> List[Dict[str, int]]:
    '''
    Return all entries which are largest in their row and are smallest in their
    column.
    '''
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("Rows must all be of equal length.")

    return ({"row": i+1, "column": j+1}
            for i, row in enumerate(matrix)
            for j, x in enumerate(row)
            if x == max(row) and x == min(row[j] for row in matrix))
