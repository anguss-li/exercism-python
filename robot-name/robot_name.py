import random
import string


class Robot:
    _names = {None, }

    def reset(self):
        while self.name in Robot._names:
            new_name = (random.choices(string.ascii_uppercase, k=2) +
                        random.choices(range(0, 9), k=3))
            self.name = ''.join(str(char) for char in new_name)
        Robot._names.add(self.name)

    def __init__(self):
        self.name = None
        self.reset()
