def format_line(line: str):
    stripped_line = line.strip()
    capitalized_line = stripped_line.upper()

    if capitalized_line.endswith("."):
        return f"{capitalized_line}.."
    else:
        return f"{capitalized_line}..."
