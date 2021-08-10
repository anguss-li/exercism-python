BY_ONE = (
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen'
)

BY_TEN = (
    'zero',
    'ten',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety'
)

PLACES = {
    100: (10, ''),
    1000: (100, 'hundred'),
    1000000: (1000, 'thousand'),
    1000000000: (1000000, 'million'),
    1000000000000: (1000000000, 'billion')
}


def say(number):
    if not 0 <= number <= 999999999999:
        raise ValueError("Number out of range.")
    elif number < 20:
        return BY_ONE[number]

    limit = min(n for n in PLACES if number < n)
    place, name = PLACES[limit]
    digit, remainder = number // place, number % place

    head = (BY_TEN[digit] if limit == 100
            else BY_ONE[digit] if limit == 1000
            else say(digit))
    spacer = '-' if limit == 100 else ' '
    tail = f'{spacer}{say(remainder)}' if remainder > 0 else ''
    return f'{head} {name}{tail}' if limit > 100 else f'{head}{name}{tail}'
