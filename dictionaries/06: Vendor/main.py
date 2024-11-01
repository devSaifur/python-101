def calculate_total(items_purchased: list, pinned_list: list):
    item_prices = {
        "health_potion": 10.00,
        "mana_potion": 12.00,
        "gold_dust": 5.00,
        "dwarven_ale": 8.00,
        "enchanted_scroll": 25.00,
        "ice_cold_milk": 50.00,
        "herbs": 7.00,
        "crystal_shard": 20.00,
        "magic_ring": 100.00,
        "mystic_amulet": 150.00,
    }

    unpurchased_items = []
    receipt = {}
    total_cost = 0

    for item in pinned_list:
        if item not in items_purchased:
            unpurchased_items.append(item)

    for item in items_purchased:
        receipt[item] = item_prices[item]
        total_cost += item_prices[item]

    return unpurchased_items, receipt, total_cost