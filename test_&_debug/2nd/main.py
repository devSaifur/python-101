def take_magic_damage(health, resist, amp, spell_power):
    maximum_damage = spell_power * amp
    actual_damage = maximum_damage - resist
    health -= actual_damage
    return health
