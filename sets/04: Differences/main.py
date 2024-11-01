def find_missing_ids(first_ids, second_ids):
    new_set = set()

    new_list = []

    for item in first_ids:
        if item not in second_ids:
            new_set.add(item)

    for item in new_set:
        new_list.append(item)

    return new_list
