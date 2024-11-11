from typing import Callable


def word_count_aggregator() -> Callable:
    count = 0

    def counter(doc: str):
        nonlocal count
        words = doc.split()
        count += len(words)
        return count

    return counter
