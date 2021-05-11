class Matrix:
    def __init__(self, matrix_string):
        '''
        matrix_string: string of numbers, "\n" denotes row break
        '''
        row_num = matrix_string.count("\n") + 1
        non_entries = str.maketrans(dict.fromkeys("\n", " "))
        matrix_entries = matrix_string.translate(non_entries).split(" ")
        column_num = int(len(matrix_entries) / row_num)
        self.matrix = []
        for row in range(row_num):
            for column in range(column_num):
                index = column + (column_num * row)
                entry = int(matrix_entries[index])
                self.matrix.append((entry, row + 1, column + 1))

    def row(self, index):
        return [entry[0] for entry in self.matrix if entry[1] == index]

    def column(self, index):
        return [entry[0] for entry in self.matrix if entry[2] == index]
