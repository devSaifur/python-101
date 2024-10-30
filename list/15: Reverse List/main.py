def reverse_array(items: list):
    new_reversed_list = []

    if items != []:
        for item in items[::-1]:
            new_reversed_list.append(item)

    return new_reversed_list
