def toggle_case(line: str):
    if line.istitle():
        return line.upper() + "!!!"
    if line.isupper():
        return line.lower().capitalize().replace("!", "")
    if len(line) > 0 and line[1:].islower():
        return line.title()
    else:
        return line
