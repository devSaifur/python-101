from typing import Callable


def lines_with_sequence(char: str) -> Callable:
    def with_char(length: int):
        sequence = char * length

        def with_length(doc: str):
            lines = doc.split("\n")
            print("PRINTING", sequence)
            num_of_lines_has_sequence = sum(1 for line in lines if sequence in line)
            return num_of_lines_has_sequence

        return with_length

    return with_char
