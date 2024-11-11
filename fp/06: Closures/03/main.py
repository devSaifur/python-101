from typing import Callable


def new_clipboard(initial_clipboard: dict) -> tuple[Callable, Callable]:
    clipboard = initial_clipboard.copy()

    def copy_to_clipboard(key: str, value: str) -> dict:
        clipboard[key] = value
        return clipboard

    def paste_from_clipboard(key: str) -> str:
        if key in clipboard:
            value = clipboard[key]
            return value
        else:
            return ""

    return copy_to_clipboard, paste_from_clipboard
