def count_vowels(text: str):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    num_of_vowels = 0
    vowels_found = set()

    words_list = text.split()

    for word in words_list:
        for latter in word:
            if latter in vowels:
                num_of_vowels += 1
                vowels_found.add(latter)

    return num_of_vowels, vowels_found
