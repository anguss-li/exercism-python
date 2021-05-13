from typing import List


class Matrix:
    def __init__(self, matrix_string: str) -> None:
        '''
        A 2D array of integers, where each element represents a row. 
        
        Args:
            matrix_string: numbers separated by spaces. "\n" is a row break.
        '''
        rows = matrix_string.splitlines()
        self.matrix = [[int(entry) for entry in row.split()] for row in rows]

    def row(self, index: int) -> List[int]:
        '''
        Return the nth row of the matrix, where n == index.
        '''
        return [entry for entry in self.matrix[index - 1]]

    def column(self, index: int) -> List[int]:
        '''
        Return a list of the nth integer in each row, where n == index.
        '''
        return [row[index - 1] for row in self.matrix]
