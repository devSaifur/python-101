from enum import Enum


class EditType(Enum):
    NEWLINE = 1
    SUBSTITUTE = 2
    INSERT = 3
    DELETE = 4


def handle_edit(document, edit_type, edit):
    lines = document.split("\n")

    if edit_type == EditType.NEWLINE:
        line_number = edit["line_number"]
        if line_number >= len(lines):
            raise Exception("Invalid line number")
        lines[line_number] += "\n"
        return "\n".join(lines)

    elif edit_type == EditType.SUBSTITUTE:
        line_number = edit["line_number"]
        start = edit["start"]
        end = edit["end"]
        insert_text = edit["insert_text"]
        if line_number >= len(lines):
            raise Exception("Invalid line number")
        if start > len(lines[line_number]):
            raise Exception("Invalid start index")
        if end > len(lines[line_number]) or end < start:
            raise Exception("Invalid end index")
        lines[line_number] = (
            lines[line_number][:start] + insert_text + lines[line_number][end:]
        )
        return "\n".join(lines)

    elif edit_type == EditType.INSERT:
        line_number = edit["line_number"]
        start = edit["start"]
        insert_text = edit["insert_text"]
        if line_number >= len(lines):
            raise Exception("Invalid line number")
        if start > len(lines[line_number]):
            raise Exception("Invalid start index")
        lines[line_number] = (
            lines[line_number][:start] + insert_text + lines[line_number][start:]
        )
        return "\n".join(lines)

    elif edit_type == EditType.DELETE:
        line_number = edit["line_number"]
        start = edit["start"]
        end = edit["end"]
        if line_number >= len(lines):
            raise Exception("Invalid line number")
        if start > len(lines[line_number]):
            raise Exception("Invalid start index")
        if end > len(lines[line_number]) or end < start:
            raise Exception("Invalid end index")
        lines[line_number] = lines[line_number][:start] + lines[line_number][end:]
        return "\n".join(lines)

    else:
        raise Exception("Unknown edit type")
