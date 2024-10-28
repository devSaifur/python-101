def main():
    health = 50
    armor = 10
    add_armer(health, armor)


def add_armer(h, a):
    new_health = h + a
    print_health(new_health)


def print_health(new_health):
    print(f"Player now has health of {new_health}")


main()


def to_celsius(f):
    celsius = (5 / 9) * (f - 32)
    return celsius


def test(f):
    c = round(to_celsius(f), 2)
    print(f"{f} degree fahrenheit is {c} degree celsius")


test(100)
test(112)
test(70)
test(50)
