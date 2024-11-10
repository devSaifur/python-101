import functools


def join(doc_so_far: str, sentence: str) -> str:
    return f"{doc_so_far}. {sentence}"


def join_first_sentences(sentences: list[str], n: int) -> str:
    if n <= 0:
        return ""

    str_list = []

    for sentence in sentences[:n]:
        str_list.append(sentence)

    string = functools.reduce(join, str_list)

    return f"{string}."
