from typing import Callable


def replacer(old: str, new: str) -> Callable:
    def replace(decorated_func: Callable) -> Callable:
        def wrapper(text: str):
            res = text.replace(old, new)
            return decorated_func(res)

        return wrapper

    return replace


@replacer("&", "&amp;")
@replacer("<", "&lt;")
@replacer(">", "&gt;")
@replacer('"', "&quot;")
@replacer("'", "&#x27;")
def tag_pre(text):
    return f"<pre>{text}</pre>"
