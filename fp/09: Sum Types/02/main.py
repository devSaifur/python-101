from enum import Enum


class DocFormat(Enum):
    PDF = 1
    TXT = 2
    MD = 3
    HTML = 4


def convert_format(content: str, from_format, to_format):
    match (from_format, to_format):
        case (DocFormat.MD, DocFormat.HTML):
            return content.replace("# ", "<h1>") + "</h1>"
        case (DocFormat.TXT, DocFormat.PDF):
            return "[PDF] " + content + " [PDF]"
        case (DocFormat.HTML, DocFormat.MD):
            content = content.replace("<h1>", "# ")
            content = content.replace("</h1>", "")
            return content
        case _:
            raise Exception("Invalid type")
