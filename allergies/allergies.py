from itertools import chain, combinations
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
        self.score = score

    def allergic_to(self, item: str) -> bool:
        return bool(self.score & Allergies.allergens[item])

    @property
    def lst(self) -> List[str]:
        return [allergen for allergen in Allergies.allergens 
                if self.allergic_to(allergen)]
