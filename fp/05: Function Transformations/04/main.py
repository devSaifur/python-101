from typing import Callable


def get_filter_cmd(filters: dict[str, Callable]) -> Callable:
    def filter_cmd(content: str, options: list[str], word_pairs: list[tuple]) -> str:
        if not options:
            raise Exception("missing options")

        filtered_content = content

        for option in options:
            if option not in filters:
                raise Exception("invalid option")
            else:
                filtered_content = filters[option](filtered_content, word_pairs)

        return filtered_content

    return filter_cmd


def replace_words(content, word_pairs):
    for pair in word_pairs:
        content = content.replace(pair[0], pair[1])
    return content


def remove_words(content, word_pairs):
    for pair in word_pairs:
        content = content.replace(pair[0], "")
    return content


def capitalize_sentences(content, word_pairs):
    return ". ".join(map(str.capitalize, content.split(". ")))


def uppercase_words(content, word_pairs):
    for pair in word_pairs:
        content = content.replace(pair[0], pair[0].upper())
    return content


filters = {
    "--replace": replace_words,
    "--remove": remove_words,
    "--capitalize": capitalize_sentences,
    "--uppercase": uppercase_words,
}
