from typing import Callable


def converted_font_size(font_size: int) -> Callable:
    def aux(doc_type: str) -> int:
        if doc_type == "txt":
            return font_size
        if doc_type == "md":
            return font_size * 2
        if doc_type == "docx":
            return font_size * 3
        raise ValueError("Invalid doc type")

    return aux
