def divide_list(nums, divisor):
    list = []

    for num in nums:
        divided_num = num // divisor
        list.append(divided_num)

    return list
