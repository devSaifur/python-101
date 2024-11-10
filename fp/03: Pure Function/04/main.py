def remove_emphasis_from_word(word: str) -> str:
    return word.strip("*")


def remove_emphasis_from_line(line: str) -> str:
    words = line.split()
    filtered_words = map(remove_emphasis_from_word, words)

    return " ".join(filtered_words)


def remove_emphasis(doc_content: str) -> str:
    lines = doc_content.split("\n")
    filtered_doc = map(remove_emphasis_from_line, lines)

    return "\n".join(filtered_doc)
