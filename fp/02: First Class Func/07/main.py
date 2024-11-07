def restore_documents(originals: tuple[str], backups: tuple[str]) -> set:
    return set(
        filter(
            lambda doc: not doc.isdigit(),
            map(lambda doc: doc.upper(), originals + backups),
        )
    )
