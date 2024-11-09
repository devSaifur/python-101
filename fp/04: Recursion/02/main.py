def zipmap(keys: list, values: list) -> dict:
    if not keys or not values:
        return {}

    dict = {}
    dict[keys[0]] = values[0]

    dict.update(zipmap(keys[1:], values[1:]))

    return dict
