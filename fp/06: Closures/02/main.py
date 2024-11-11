from typing import Callable


def new_collection(initial_docs: list[str]) -> Callable:
    docs = initial_docs.copy()

    def make_copy(new_docs: str):
        docs.append(new_docs)
        return docs

    return make_copy
