from itertools import chain
from typing import List

STUDENTS = ['Alice',
            'Bob',
            'Charlie',
            'David',
            'Eve',
            'Fred',
            'Ginny',
            'Harriet',
            'Ileana',
            'Joseph',
            'Kincaid',
            'Larry']

PLANTS = {'C': 'Clover',
          'G': 'Grass',
          'R': 'Radishes',
          'V': 'Violets'}


class Garden:
    """
    Rows of plants taken care of by kindergarten students. Each student is
    responsible for the n-th column of the garden, where n is determined by
    their name order and each column is 2 plants wide.

    Attributes:
        diagram: type of plant in each position in the rows
        students: students taking care of the plants
    """

    def __init__(self, diagram: str, students: List[str] = STUDENTS):
        """Determine which plants each student takes care of."""
        diagram = diagram.splitlines()
        assert all(len(row) == (row_len := len(diagram[0])) for row in diagram)

        self.students = sorted(students)
        columns = (chain.from_iterable((row[n], row[n+1]) for row in diagram)
                   for n in range(0, row_len, 2))

        self.ownership = {student: [PLANTS[plant] for plant in column]
                          for student, column in zip(self.students, columns)}

    def plants(self, student: str) -> List[str]:
        """Return the plants a student is responsible for."""
        return self.ownership[student]
