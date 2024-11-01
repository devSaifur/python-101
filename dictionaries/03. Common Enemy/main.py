def get_most_common_enemy(enemies_dict):
    if not enemies_dict:
        return

    max_so_far = float("-inf")
    common_enemy = ""

    for enemy in enemies_dict:
        num_of_enemy = enemies_dict[enemy]

        if num_of_enemy > max_so_far:
            max_so_far = num_of_enemy
            common_enemy = enemy

    return common_enemy
