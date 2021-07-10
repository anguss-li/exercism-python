from typing import List


def recite(start_verse: int, end_verse: int) -> List[str]:
    '''Print the Twelve Days of Christmas from the start verse to the end'''

    def ordinal(number: int) -> str:
        endings = (
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
        return endings[number - 1]

    gifts = {
        1: 'a Partridge in a Pear Tree.',
        2: 'two Turtle Doves,',
        3: 'three French Hens,',
        4: 'four Calling Birds,',
        5: 'five Gold Rings,',
        6: 'six Geese-a-Laying,',
        7: 'seven Swans-a-Swimming,',
        8: 'eight Maids-a-Milking,',
        9: 'nine Ladies Dancing,',
        10: 'ten Lords-a-Leaping,',
        11: 'eleven Pipers Piping,',
        12: 'twelve Drummers Drumming,'
    }

    verses = []
    for day in range(start_verse, end_verse + 1):
        verse = [f'On the {ordinal(day)} day of Christmas my true love gave to me:']
        verse.extend([gifts[day] for day in range(day, 0, -1)])
        if day > 1:
            verse.insert(-1, "and")
        verses.append(" ".join(verse))

    return verses