def fizzbuzz(start, end):
    for num in range(start, end + 1):
        if num % 3 == 0:
            print("Fizz")
            continue
        if num % 5 == 0:
            print("Buzz")
            continue
        if num % 3 == 0 and num % 5 == 0:
            return print("FizzBuzz")
        else:
            print(num)


def main():
    test(1, 100)
    test(5, 30)
    test(1, 15)


def test(start, end):
    print("Starting test")
    fizzbuzz(start, end)
    print("======================")


main()
