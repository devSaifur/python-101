def remove_nonints(nums):
    ints = []

    for num in nums:
        if type(num) is int:
            ints.append(num)

    return ints
