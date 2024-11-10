from typing import Callable


def doc_format_checker_and_converter(
    conversion_function: Callable, valid_formats: list
) -> Callable:
    def check_validity(filename: str, content: str):
        ext = filename.split(".")[1]
        if ext in valid_formats:
            return conversion_function(content)
        else:
            raise ValueError("Invalid file format")

    return check_validity


def capitalize_content(content: str) -> str:
    return content.upper()


def reverse_content(content: str) -> str:
    return content[::-1]
