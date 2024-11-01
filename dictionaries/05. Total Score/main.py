def merge(dict1, dict2):
    dict1.update(dict2)
    return dict1


def total_score(score_dict):
    score = 0

    for s in score_dict:
        score += score_dict[s]

    return score
