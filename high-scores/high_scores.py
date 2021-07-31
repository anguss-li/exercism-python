from typing import List


def latest(scores: List[int]) -> int:
    '''Find the latest score in scores.'''
    return scores[-1]


def personal_best(scores: List[int]) -> int:
    '''Find the highest score in scores.'''
    return max(scores)


def personal_top_three(scores: List[int]) -> List[int]:
    '''Find the highest 3 scores in scores.'''
    return sorted(scores, reverse=True)[:3]
