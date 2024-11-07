valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]


def pair_document_with_format(doc_names: list, doc_formats: list) -> filter[tuple]:
    docs = zip(doc_names, doc_formats)

    valid_docs = filter(lambda fmt: fmt[1] in valid_formats, docs)

    return valid_docs
