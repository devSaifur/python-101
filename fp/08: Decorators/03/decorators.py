from typing import Callable


def markdown_to_text_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        args_lst = list(map(convert_md_to_txt, args))
        kwargs_dct = dict(
            map(lambda x: (x[0], convert_md_to_txt(x[1])), kwargs.items())
        )

        return func(*args_lst, **kwargs_dct)

    return wrapper


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)
