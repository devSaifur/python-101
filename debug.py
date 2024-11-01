def fizzbuzz(start, end):
    for num in range(start, end + 1):
        if num % 3 == 0:
            print("FIZZ")
            continue
        if num % 5 == 0:
            print("BUZZ")
            continue
        if num % 3 == 0 and num % 5 == 0:
            return print("FIZZBUZZ")
        else:
            print(num)


fizzbuzz(0, 10)
