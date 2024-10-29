def calculate_experience_points(levels):
    total_xp = 0
    xp_needed = 0

    for level in range(1, levels):
        xp_needed = level * 5
        total_xp += xp_needed - 5

    return total_xp + xp_needed
