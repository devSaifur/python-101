from typing import Callable


def create_markdown_image(alt_text: str) -> Callable[[str], Callable[[str], str]]:
    alt = f"![{alt_text}]"

    def inner_fn(url: str) -> Callable[[str], str]:
        valid_url = f"({url.replace('(', '%28').replace(')', '%29')}"
        full_url = alt + valid_url

        def inner_most_fn(title: str = "") -> str:
            if title:
                valid_title = f' "{title}"'
                return full_url + valid_title + ")"
            else:
                return full_url + ")"

        return inner_most_fn

    return inner_fn
