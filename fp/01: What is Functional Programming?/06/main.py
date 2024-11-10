def hex_to_rgb(hex_color):
    is_valid_hex = is_hexadecimal(hex_color)
    if is_valid_hex is False:
        raise Exception("not a hex color string")

    r = int(hex_color[:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:], 16)
    return r, g, b


def is_hexadecimal(hex_string):
    try:
        if len(hex_string) < 6:
            return False
        int(hex_string, 16)
        return True
    except Exception:
        return False
