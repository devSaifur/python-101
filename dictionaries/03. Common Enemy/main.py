def get_most_common_enemy(enemies_dict):
    if enemies_dict == {}:
        return None

    max_so_far = float("-inf")
    common_enemy = ""

    for enemy in enemies_dict:
        if enemy is None:
            return None

        num_of_enemy = enemies_dict[enemy]

        if num_of_enemy > max_so_far:
            max_so_far = num_of_enemy
            common_enemy = enemy

    return common_enemy
