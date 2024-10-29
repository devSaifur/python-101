def has_enough_energy(energy_available, distance_one_way, meters_per_energy):
    total_distance = distance_one_way * 2
    energy_needed = total_distance / meters_per_energy

    if energy_available >= energy_needed:
        return True
    else:
        return False
