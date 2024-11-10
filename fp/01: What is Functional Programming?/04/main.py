def format_line(line: str):
    stripped = line.strip()
    capitalized = stripped.upper()
    no_periods = capitalized.replace(".", "")

    return f"{no_periods}..."
