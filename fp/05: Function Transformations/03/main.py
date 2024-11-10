from typing import Callable


def get_filter_cmd(filter_one: Callable, filter_two: Callable) -> Callable:
    def filter_cmd(content: str, option="--one"):
        if option == "--one":
            return filter_one(content)
        if option == "--two":
            return filter_two(content)
        if option == "--three":
            res = filter_one(content)
            return filter_two(res)
        else:
            raise Exception("invalid option")

    return filter_cmd


def replace_bad(text):
    return text.replace("bad", "good")


def replace_ellipsis(text):
    return text.replace("..", "...")


def fix_ellipsis(text):
    return text.replace("....", "...")
