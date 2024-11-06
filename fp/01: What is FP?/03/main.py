def get_median_font_size(font_sizes: list):
    if len(font_sizes) == 0:
        return None
    else:
        sorted_font_sizes = sorted(font_sizes)
        middle = len(sorted_font_sizes) // 2
        if len(sorted_font_sizes) % 2 == 0:
            return sorted_font_sizes[middle - 1]
        else:
            return sorted_font_sizes[middle]
