def smelt_ore(inventory):
    if inventory[1] is None:
        inventory[1] = None
    else:
        inventory[1] = "Iron Bar"

    return inventory
