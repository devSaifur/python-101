def area_sum(rectangles):
    sum = 0

    for rect in rectangles:
        height = rect["height"]
        width = rect["width"]
        sum = sum + (height * width)

    return sum
