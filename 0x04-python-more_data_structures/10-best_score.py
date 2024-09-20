#!/usr/bin/python3
def best_score(a_dictionary: dict):
    best = 0
    winner = ''
    if not a_dictionary:
        return None
    for key, val in a_dictionary.items():
        if val > best:
            best = val
            winner = key

    return winner
