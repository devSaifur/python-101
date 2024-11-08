def add_format(default_formats: dict, new_format: str) -> dict:
    new_fmt = dict(default_formats)
    new_fmt[new_format] = True
    return new_fmt


def remove_format(default_formats: dict, old_format: str) -> dict:
    new_fmt = dict(default_formats)
    new_fmt[old_format] = False
    return new_fmt
