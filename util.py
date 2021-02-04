import random

def random_weighted_choice(pairs):
    """
    :param pairs: list of (option, weight) pairs
    """
    total = sum((pair[1] for pair in pairs))
    r = random.randint(1, total)

    for option, weight in pairs:
        r -= weight
        if r <= 0:
            return option