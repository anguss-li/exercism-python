class Matrix:
    def __init__(self, matrix_string):
        '''
        matrix_string: string of numbers, "\n" denotes row break
        '''
        rows = matrix_string.split("\n")
        self.matrix = [list(map(int, row.split(" "))) for row in rows]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]
