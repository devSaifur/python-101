def change_bullet_style(document: str):
    doc = list(map(convert_line, document))

    return "".join(doc)


def convert_line(line: str):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
