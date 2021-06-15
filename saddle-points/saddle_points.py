from typing import List, Dict


def saddle_points(matrix: list) -> List[Dict[str, int]]:
    '''
    Return all entries which are largest in their row and are smallest in their
    column.
    '''
    if len(matrix) > 0 and any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("Rows must all be of equal length.")

    def get_row_index(value: int) -> List[int]:
        '''
        Return indices of all entries equal to value in row.
        '''
        return [index + 1 for index, x in enumerate(row) if x == value]

    def get_column_min(index: List[int]) -> List[int]:
        '''
        Return the smallest entry in the inth column.
        '''
        return min([row[index - 1] for row in matrix])

    point_list = []

    for row_num, row in enumerate(matrix, 1):
        row_highest = max(row)
        column_num = get_row_index(row_highest)
        for num in column_num:
            column_min = get_column_min(num)
            if row_highest == column_min:
                saddle_point = {"row": row_num, "column": num}
                point_list.append(saddle_point)

    return point_list
