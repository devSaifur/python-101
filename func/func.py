def aria_of_circle(radius):
    pi = 3.14
    aria = pi * radius * radius
    return aria


sword_length = 1.0
spear_length = 2.0


sword_aria = aria_of_circle(sword_length)
spear_aria = aria_of_circle(spear_length)

print(f"Sword length {sword_length} meters")
print(f"Sword attack aria {sword_aria} squire meters")

print(f"Spear length {spear_length} meters")
print(f"Spear attack aria {spear_aria} squire meters")


def get_details():
    name = "Saifur Rahman"
    age = 24
    return name, age


def show_details():
    name, age = get_details()
    print(f"My name is {name}, and I'm {age} years old")


show_details()
