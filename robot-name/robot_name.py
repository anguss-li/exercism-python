from random import choices
from string import ascii_uppercase as letters


class Robot:
    _names = {None, }

    def reset(self):
        while self.name in Robot._names:
            new_name = (choices(letters, k=2) + choices(range(0, 9), k=3))
            self.name = ''.join(str(char) for char in new_name)
        Robot._names.add(self.name)

    def __init__(self):
        self.name = None
        self.reset()
