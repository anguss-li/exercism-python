from operator import add, floordiv, mul, sub
from re import split

OPERATIONS = {
    'plus': add,
    'minus': sub,
    'multiplied by': mul,
    'divided by': floordiv
}


def answer(question: str) -> int:
    """Calculate the answer to a simple maths word problem."""
    phrases = split(r' (?!\bby\b)', question.replace('?', ''))
    length = len(phrases)-1

    if not any(word in OPERATIONS for word in phrases):
        try:
            return int(phrases[-1])
        except TypeError:
            raise ValueError('No numbers and/or operators in question.')

    stack = []

    for i, word in enumerate(phrases):
        if word.isdigit() and i != length and phrases[i+1] not in OPERATIONS:
            raise ValueError('Missing operation.')
        elif word not in OPERATIONS:
            continue

        try:
            a, b = stack[-1] if stack else int(phrases[i-1]), int(phrases[i+1])
        except (TypeError, IndexError):
            raise ValueError('Numbers not in valid order.')

        stack.append(OPERATIONS[word](a, b))

    return stack.pop()
