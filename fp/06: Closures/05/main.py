from typing import Callable


def css_styles(initial_styles: dict[str, dict]) -> Callable:
    styles = initial_styles.copy()

    def add_style(selector: str, property: str, value: str) -> dict[str, dict]:
        if selector not in styles:
            styles[selector] = {property: value}
            return styles
        else:
            existing_styles = styles[selector]
            existing_styles.update({property: value})
            return styles

    return add_style
