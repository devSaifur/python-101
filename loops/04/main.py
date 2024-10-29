def calculate_flurry_crit(num_attacks, base_damage):
    total_damage = base_damage * 2
    last_attack = num_attacks

    for attack in range(0, num_attacks):
        if attack != last_attack:
            total_damage += base_damage * 2
        else:
            total_damage += base_damage * 4

    return total_damage
