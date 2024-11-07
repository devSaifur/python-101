def file_type_getter(file_extension_tuples: list):
    dict = {}
    for item in file_extension_tuples:
        key, value = item
        for type in value:
            dict[type] = key

    return lambda type: dict.get(type, "Unknown")
