def word_count_memo(document: str, memos: dict) -> tuple[int, dict]:
    memo_docs = memos.copy()

    if document in memo_docs:
        return memo_docs[document], memo_docs

    word_count = get_word_count(document)
    memo_docs[document] = word_count

    return word_count, memo_docs


def get_word_count(document: str) -> int:
    count = len(document.split())
    return count
