def count_nested_levels(
    nested_documents: dict, target_document_id: int, level=1
) -> int:
    for node, child_documents in nested_documents.items():
        if node == target_document_id:
            return level
        elif isinstance(child_documents, dict) and child_documents:
            result = count_nested_levels(child_documents, target_document_id, level + 1)
            if result != -1:
                return result
    return -1
