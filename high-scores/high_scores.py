def latest(scores):
    '''
    scores: list of ints, scores from game
    returns: last integer in scores
    '''
    return scores[-1]


def personal_best(scores):
    '''
    scores: list of ints, scores from game
    returns: largest integer in scores
    '''
    return max(scores)


def personal_top_three(scores):
    '''
    scores: list of ints, scores from game
    returns: largest 3 integers in scores
    '''
    return sorted(scores, reverse=True)[:3]
