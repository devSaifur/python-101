from functools import reduce
from typing import Callable


def create_tagger(tag):
    def tagger(content):
        return f"<{tag}>{content}</{tag}>"

    return tagger


def create_accumulator(tagger):
    def accumulate(items):
        return reduce(lambda acc, item: acc + tagger(item), items, "")

    return accumulate


tag_data = create_tagger("td")
tag_header = create_tagger("th")
tag_row = create_tagger("tr")
tag_table = create_tagger("table")

accumulate_data_cells = create_accumulator(tag_data)
accumulate_rows = create_accumulator(tag_row)
accumulate_headers = create_accumulator(tag_header)


def create_html_table(data_rows: list[str]) -> Callable:
    data_cells = map(lambda x: accumulate_data_cells(x), data_rows)
    data_raws = accumulate_rows(list(data_cells))

    def create_table_headers(headers: list[str]):
        nonlocal data_raws
        headers_cells = accumulate_headers(headers)
        header_rows = tag_row(headers_cells)

        table_body = header_rows + data_raws
        table = tag_table(table_body)
        return table

    return create_table_headers
