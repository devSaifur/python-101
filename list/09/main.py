def get_champion_slices(champions):
    third_to_end = champions[2:]
    first_to_third = champions[:-2]
    even_index = champions[::2]

    return third_to_end, first_to_third, even_index
