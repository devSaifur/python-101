my_dict = {"apple": 5, "banana": 3, "cherry": 7}

key_value_map = map(lambda x: (x[0], x[1]), my_dict.items())

# Convert the map object to a list
key_value_pairs = list(key_value_map)

print(key_value_pairs)


print([(key, value) for key, value in my_dict.items()])
