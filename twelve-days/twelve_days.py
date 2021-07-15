from typing import List


VERSES = (
    ("On the", "day of Christmas my true love gave to me:"),
    ("first", "a Partridge in a Pear Tree."),
    ("second", "two Turtle Doves, and"),
    ("third", "three French Hens,"),
    ("fourth", "four Calling Birds,"),
    ("fifth", "five Gold Rings,"),
    ("sixth", "six Geese-a-Laying,"),
    ("seventh", "seven Swans-a-Swimming,"),
    ("eighth", "eight Maids-a-Milking,"),
    ("ninth", "nine Ladies Dancing,"),
    ("tenth", "ten Lords-a-Leaping,"),
    ("eleventh", "eleven Pipers Piping,"),
    ("twelfth", "twelve Drummers Drumming,")
)


def recite(start_verse: int, end_verse: int) -> List[str]:
    '''Print the Twelve Days of Christmas from the start verse to the end'''

    def gifts(day: int) -> str:
        gifts = [phrase for phrase in VERSES[0]]
        gifts.insert(-1, VERSES[day][0])
        gifts.extend([VERSES[verse][1] for verse in range(day, 0, -1)])
        return " ".join(gifts)

    return [gifts(day) for day in range(start_verse, end_verse + 1)]
