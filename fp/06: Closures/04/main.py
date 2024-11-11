from typing import Callable


def user_words(initial_words: tuple[str]) -> Callable:
    words = list(initial_words)

    def add_word(new_word: str) -> tuple:
        words.append(new_word)
        return tuple(words)

    return add_word
