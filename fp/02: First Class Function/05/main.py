def get_common_formats(formats1: list, formats2: list) -> set:
    fmt1 = set(formats1)
    fmt2 = set(formats2)

    return fmt1.intersection(fmt2)
