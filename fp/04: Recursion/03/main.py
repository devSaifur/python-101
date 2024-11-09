def sum_nested_list(lst: list) -> int:
    total_sum = 0

    for item in lst:
        total_sum += sum_nested_list(item) if isinstance(item, list) else item

    return total_sum
