def index_keywords(
    document: str, index: dict[str, list[str]]
) -> tuple[list[str], dict[str, list[str]]]:
    index_copy = index.copy()

    if document in index_copy:
        return index_copy[document], index_copy

    found_keywords = find_keywords(document)
    index_copy[document] = found_keywords
    return found_keywords, index_copy


def find_keywords(document: str) -> list:
    keywords = [
        "functional",
        "immutable",
        "declarative",
        "higher-order",
        "lambda",
        "deterministic",
        "side-effects",
        "memoization",
        "referential transparency",
    ]

    return list(filter(lambda keyword: keyword in document, keywords))
