def filter_messages(messages):
    filtered = []
    num_of_removed_words = []

    for message in messages:
        words = message.split(" ")
        filtered_words = [word for word in words if word != "dang"]
        filtered_message = " ".join(filtered_words)

        filtered.append(filtered_message)

        num_removed = words.count("dang")
        num_of_removed_words.append(num_removed)

    return filtered, num_of_removed_words
