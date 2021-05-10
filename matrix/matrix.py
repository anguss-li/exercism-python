class Matrix:
    def __init__(self, matrix_string):
        '''
        matrix_string: string of numbers, "\n" denotes row break
        '''
        row_num = matrix_string.count("\n") + 1
        non_entries = str.maketrans(dict.fromkeys("\n", " "))
        matrix_entries = matrix_string.translate(non_entries).split(" ")
        column_num = int(len(matrix_entries) / row_num)
        self.matrix = {}
        for row in range(row_num):
            for column in range(column_num):
                coords = (row + 1, column + 1)
                index = column + (column_num * row)
                self.matrix[coords] = int(matrix_entries[index])

    def row(self, index):
        matrix = self.matrix
        return [matrix[coords] for coords in matrix if coords[0] == index]

    def column(self, index):
        matrix = self.matrix
        return [matrix[coords] for coords in matrix if coords[1] == index]
