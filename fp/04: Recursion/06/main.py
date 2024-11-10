def reverse_string(s: str) -> str:
    if len(s) == 0:
        return ""

    return s[-1] + reverse_string(s[:-1])
