from typing import List

class Allergies:
    allergens = {
        'eggs': 1,
        'peanuts': 2,
        'shellfish': 4,
        'strawberries': 8,
        'tomatoes': 16,
        'chocolate': 32,
        'pollen': 64,
        'cats': 128
    }

    def __init__(self, score: int):
        '''Record items that an individual is allergic to from allergens.'''
        self.score = score

    def allergic_to(self, item: str) -> bool:
        '''Check whether the individual is allergic to item.'''
        # '&' returns whether the binary versions of two numbers both have '1'
        # in the same digit. As all allergy scores are multiples of 2 (10 in 
        # binary), this can be used to quickly check if a given multiple of 2
        # is in a given number.
        return bool(self.score & Allergies.allergens[item])

    @property
    def lst(self) -> List[str]:
        '''List all objects that the individual is allergic to.'''
        return [allergen for allergen in Allergies.allergens 
                if self.allergic_to(allergen)]
