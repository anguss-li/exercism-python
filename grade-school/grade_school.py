class School:
    def __init__(self):
        """Store the names and grades of school students."""
        self.students = {}

    def add_student(self, name: str, grade: int) -> None:
        """Add a student to a grade in the roster."""
        school_grade = self.students.setdefault(grade, [])
        school_grade.append(name)
        school_grade.sort()

    def roster(self) -> list:
        """Find all students in the school regardless of grade."""
        return [student
                for grade in sorted(self.students)
                for student in self.students[grade]]

    def grade(self, grade_number: int):
        """Find all students in a particular grade."""
        return self.students.setdefault(grade_number, [])
