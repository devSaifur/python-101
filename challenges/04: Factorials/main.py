def factorial(num):
    fact = 0
    current_index = 1

    for i in range(0, num + 1):
        if i != 0:
            fact = current_index * i
            current_index = fact
        else:
            fact = 1

    return fact
