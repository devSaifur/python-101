def deduplicate_lists(lst1, lst2, reverse=False):
    merged_list = [*lst1, *lst2]
    list_with_unique_item = list(set(merged_list))

    return sorted(list_with_unique_item, reverse=reverse)
