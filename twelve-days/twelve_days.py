from typing import List


ENDINGS = (
    'first',
    'second',
    'third',
    'fourth',
    'fifth',
    'sixth',
    'seventh',
    'eighth',
    'ninth',
    'tenth',
    'eleventh',
    'twelfth'
)

GIFTS = (
    'a Partridge in a Pear Tree.',
    'two Turtle Doves, and',
    'three French Hens,',
    'four Calling Birds,',
    'five Gold Rings,',
    'six Geese-a-Laying,',
    'seven Swans-a-Swimming,',
    'eight Maids-a-Milking,',
    'nine Ladies Dancing,',
    'ten Lords-a-Leaping,',
    'eleven Pipers Piping,',
    'twelve Drummers Drumming,'
)

def recite(start_verse: int, end_verse: int) -> List[str]:
    '''Print the Twelve Days of Christmas from the start verse to the end'''

    def first_line(day: int) -> str:
        return f'On the {ENDINGS[day]} day of Christmas my true love gave to me:'

    def gifts(day: int) -> str:
        gifts = [first_line(day)]
        gifts.extend([GIFTS[day] for day in reversed(range(0, day + 1))])
        return " ".join(gifts)

    return [gifts(day) for day in range(start_verse - 1, end_verse)]