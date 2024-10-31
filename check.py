recipe = ["Dragon Scale", "Unicorn Hair", "Phoenix Feather", "Troll Tusk"]
ing = ["Dragon Scale", "Goblin Ear", "Phoenix Feather", "Troll Tusk"]


missing = ["Unicorn Hair"]

percent = 100 - ((len(missing) / len(ing)) * 100)


print(percent)
