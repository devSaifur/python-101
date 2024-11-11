from typing import Callable


def new_resizer(max_width: int, max_height: int) -> Callable:
    def inner_fn(min_width=0, min_height=0) -> Callable:
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")

        def inner_most_fn(width: int, height: int) -> tuple[int, int]:
            new_width = max(min_width, min(max_width, width))
            new_height = max(min_height, min(max_height, height))

            return new_width, new_height

        return inner_most_fn

    return inner_fn
