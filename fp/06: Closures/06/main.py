from functools import reduce
from typing import Callable


def paginator(page_length: int) -> Callable:
    def paginate(document):
        words = document.split()

        def add_word_to_pages(pages: list[str], word: str):
            if not pages:
                return [word]

            current_page = pages[-1]
            if len(current_page + " " + word) <= page_length:
                return pages[:-1] + [current_page + " " + word]
            else:
                return pages + [word]

        return reduce(add_word_to_pages, words, [])

    return paginate
