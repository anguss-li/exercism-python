from itertools import chain, combinations
from typing import List


class Allergies:
    def __init__(self, score: int):
        self.allergens = {
            'eggs': 1,
            'peanuts': 2,
            'shellfish': 4,
            'strawberries': 8,
            'tomatoes': 16,
            'chocolate': 32,
            'pollen': 64,
            'cats': 128
        }
        self.scores = self.allergens.values()
        self.powerset = chain.from_iterable(combinations(self.scores, r) for r in range(len(self.scores) + 1))
        self.score = score
        while self.score > 255:
            self.score -= 256
        (self.factors,) = (subset for subset in self.powerset if sum(subset) == self.score)

    def allergic_to(self, item: str) -> bool:
        allergen_score = self.allergens[item]
        return allergen_score in self.factors

    @property
    def lst(self) -> List[str]:
        return [name for name, score in self.allergens.items() for x in self.factors if score == x]
