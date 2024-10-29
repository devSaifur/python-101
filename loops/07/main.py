def meditate(mana, max_mana, energy, energy_potions):
    while mana < max_mana and (energy > 0 or energy_potions > 0):
        if energy == 0 and energy_potions > 0:
            energy += 50
            energy_potions -= 1
            continue

        energy -= 1
        mana += 3

        if mana > max_mana:
            mana = max_mana

    return mana, energy, energy_potions
