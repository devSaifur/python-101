def find_longest_word(document: str, longest_word="") -> str:
    if not document:
        return longest_word

    words = document.split()

    if not words:
        return longest_word

    current_word = words[0]

    if len(current_word) > len(longest_word):
        longest_word = current_word

    return find_longest_word(" ".join(words[1:]), longest_word)
