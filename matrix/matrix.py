class Matrix:
    def __init__(self, matrix_string: str) -> None:
        '''
        A 2D array of integers, where each element represents a row. 
        
        Rows are split according to the delimiter "\n" in matrix_string.
        '''
        rows = matrix_string.splitlines()
        self.matrix = [[int(entry) for entry in row.split()] for row in rows]

    def row(self, index: int) -> list:
        '''
        Returns the nth row of the matrix, where n == index.
        '''
        return self.matrix[index - 1]

    def column(self, index: int) -> list:
        '''
        Returns a list of the nth integer in each row, where n == index.
        '''
        return [row[index - 1] for row in self.matrix]
