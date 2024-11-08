default_commands = {}
default_formats = ["txt", "md", "html"]
saved_documents = {}


def add_custom_command(commands: dict, new_command: str, function: str) -> dict:
    commands_copy = commands.copy()
    commands_copy[new_command] = function
    return commands_copy


def add_format(formats: list, format: str) -> list:
    formats_copy = formats.copy()
    formats_copy.append(format)
    return formats_copy


def save_document(docs: dict, file_name: str, doc: str) -> dict:
    docs_copy = docs.copy()
    docs_copy[file_name] = doc
    return docs_copy


def add_line_break(line) -> str:
    return line + "\n\n"
