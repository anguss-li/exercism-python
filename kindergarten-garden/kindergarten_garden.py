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
    '''
    Rows of plants taken care of by kindergarten students.

    Attributes:
        diagram: type of plant in each position in the rows
        students: students taking care of the plants
    '''

    def __init__(self, diagram: str, students: List[str] = STUDENTS):
        '''Clean inputs'''
        self.diagram = diagram.splitlines()
        self.students = sorted(students)

    def plants(self, student: str) -> List[str]:
        '''Return plants student is responsible for'''
        n = self.students.index(student) * 2
        seeds = (self.diagram[0][n],
                 self.diagram[0][n+1],
                 self.diagram[1][n],
                 self.diagram[1][n+1])
        return [PLANTS[seed] for seed in seeds]
