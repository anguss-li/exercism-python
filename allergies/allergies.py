from dataclasses import dataclass
from typing import List

ALLERGENS = {
    'eggs': 1,
    'peanuts': 2,
    'shellfish': 4,
    'strawberries': 8,
    'tomatoes': 16,
    'chocolate': 32,
    'pollen': 64,
    'cats': 128
}


@dataclass
class Allergies:
    '''Record items that an individual is allergic to from allergens.'''
    score: int

    def allergic_to(self, item: str) -> bool:
        '''Check whether the individual is allergic to item.'''
        # '&' returns whether the binary versions of two numbers both have '1'
        # in the same digit. As all allergy scores are multiples of 2 (10 in
        # binary), this can be used to quickly check if a given multiple of 2
        # is in a given number.
        return bool(self.score & ALLERGENS[item])

    @property
    def lst(self) -> List[str]:
        '''List all objects that the individual is allergic to.'''
        return [allergen 
                for allergen in ALLERGENS
                if self.allergic_to(allergen)]
